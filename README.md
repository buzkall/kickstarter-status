# Kickstarter Status Notificator
Get almost real time notifications of your Kickstarter campaigns (or spy others) using the stats json file from 
the kickstarter page.

<p align="center">
    <img src="https://i.imgur.com/NjLlBrQ.png" alt="kickstarter_status_schema">
</p>



The file contains this info:
```
{
  "project": {
    "id": 2003798126,
    "state_changed_at": 1518620843,
    "state": "live",
    "backers_count": 18989,
    "pledged": "3482190.0",
    "comments_count": 940
  }
}
```

## Install and Config
This script has been tested with python 2.7 and python 3 and the cron has been set on a mac with Notifier installed.
Create a virtual environment and install the requirements with pip

    virtualenv -p python3 venv
    pip3 install -r requirements.txt

In case pync fails to install you can install it with the following command [from pync repo page](https://github.com/SeTeM/pync)
    
    pip install git+https://github.com/SeTeM/pync.git 


## Usage
You can manually invoke the python script and will only get notifications if the values have changed, but the easiest
way of using it is configuring a cron task that will check changes every minute.


    * * * * * python ~/YOUR_PATH/getKickstarterStatus.py COMPANY PROJECT
    

For example: if you want to get notifications from the campaign: 
https://www.kickstarter.com/projects/597538543/the-worlds-best-travel-jacket-with-25-features-bau

The company will be 597538543 (or a name if they have claimed their url)
and the project: the-worlds-best-travel-jacket-with-25-features-bau

So you should call the script like this:

    python ~/YOUR_PATH/getKickstarterStatus.py 597538543 the-worlds-best-travel-jacket-with-25-features-bau


It will generate a file called kickstarter_cache.out.db which will save the actual values and will notify you when they change.


<p align="center">
    <img src="https://i.imgur.com/RmXGKhq.png" alt="notification kickstarter">
</p>