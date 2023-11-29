import requests
import json
import os
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import datetime
import pytz

# Secrets
API_KEY = os.environ["FLYBOOK_API_KEY"]
SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

# Variables
DATA_FILE = os.environ["LOCAL_DATA_FILE"]
NUMBER_OF_PEOPLE = 8
url = "https://go.theflybook.com/vx/activities/24192/possibleDaysToBook/" + str(NUMBER_OF_PEOPLE)
headers = {
    "X-Fb-Api-Key": API_KEY
}

start_date = datetime.datetime(year=2023, month=12, day=1)
end_date = datetime.datetime(year=2024, month=5, day=1)

def fetch_existing_data():
    """Fetch the existing data from the json file."""
    try:
        with open(DATA_FILE, "r") as f:
            old_data = json.load(f)
        return old_data
    except FileNotFoundError:
        # TODO: Send a notification
        print("Initial file not found.")
        return None
    except json.decoder.JSONDecodeError:
        # TODO: Send a notification
        print("Unable to decode JSON.")
        return None


def fetch_data_from_website(start_date, end_date):
    """Fetch the data from the website."""
    index_date = start_date
    data = {}
    while index_date < end_date:
        end_index = index_date + relativedelta(months=1)
        response = requests.post(url, headers=headers, json={'end': end_index.isoformat() + "Z", 'start': index_date.isoformat() + "Z"})
        data[index_date.isoformat()] = response.json()
        index_date = end_index
    return data

def write_data_to_file(data):
    """Write the new data to file."""
    with open(DATA_FILE, "w") as f:
        json.dump(new_data, f)

def find_mismatched_dates(old_data, new_data):
    """Given two sets of data, check for differences."""
    result = []
    if not old_data:
        return []
    
    for month in new_data.keys():
        for date in new_data[month]:
            if date not in old_data[month]:
                result.append(date)
    return result

def send_notifications(mismatched_dates):
    if not mismatched_dates:
        return
    
    message = "*<https://yosemite.org/experience/ostrander-ski-hut|Ostrander Hut> Availability!*\n"
    date_strings = []
    for date in mismatched_dates:
        date_str = ""
        val = parse(date)
        if val.weekday() >= 5:
            date_str += ":weekend: "
        date_str += "`" + val.strftime("%-m/%-d") + "`"
        date_strings.append(date_str)
    message += ", ".join(date_strings)
    
    requests.post(SLACK_WEBHOOK_URL, json={"text": message})

old_data = fetch_existing_data()
new_data = fetch_data_from_website(start_date, end_date)
write_data_to_file(new_data)
mismatched_dates = find_mismatched_dates(old_data, new_data)
send_notifications(mismatched_dates)
