# -*- coding: utf-8 -*-
from jsondiff import diff
from pync import Notifier

import requests
import shelve
import os.path
import argparse
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

KICKSTARTER_URL = 'https://www.kickstarter.com/projects/COMPANY/PROJECT/stats.json?v=1'
CACHE_PATH = dir_path + '/kickstarter_cache.out'
MAXIMUM_CACHE_DURATION = 60 * 60 * 24 * 7  # One week


def notify_native(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


parser = argparse.ArgumentParser(description='''Get your Kickstarter stats. ''', epilog="""---""")
parser.add_argument('kickstarter_company', type=str, default='', help='Your company')
parser.add_argument('kickstarter_project', type=str, default='', help='Your project')
args = parser.parse_args()

cached_data = shelve.open(CACHE_PATH)

s = requests.Session()

company_name = args.kickstarter_company
project_name = args.kickstarter_project

tmp = KICKSTARTER_URL.replace('COMPANY', company_name)
json_url = KICKSTARTER_URL.replace('PROJECT', project_name)

current_data = s.get(json_url).json()

if project_name in cached_data:
    changes = diff(cached_data[project_name]['project'], current_data['project'])

    if changes:
        Notifier.notify('Modification: ' + ''.join('{}: {} '.format(key, val) for key, val in changes.items()),
                        title='Kickstarter change ' + project_name)
        # notify_native("Kickstarter change", "Modification: " + ''.join('{}: {} '.format(key, val) for key, val in changes.items()))

        cached_data[project_name] = current_data
else:
    cached_data[project_name] = current_data

cached_data.close()
