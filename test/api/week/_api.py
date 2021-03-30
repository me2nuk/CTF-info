from datetime import datetime, timedelta
import requests
import config

global_url = "https://www.googleapis.com/calendar/v3/calendars/%s/events?orderBy=startTime&singleEvents=true&timeMin={}&timeMax={}&key=%s"% (config.calendars_Id, config.auth_key)

class calendar:
    def __init__(self, MINTime, MAXTime) -> None:
        self.MINTime = MINTime
        self.MAXTime = MAXTime
        self.url = global_url.format(self.MINTime, self.MAXTime)

    def urlopen(self) -> dict:
        calendar_urlOpens = requests.get(self.url)
        return calendar_urlOpens.json()

week_ago = (datetime.today() - timedelta(7)).strftime("%Y-%m-%dT00:00:00Z")
week_later = (datetime.today() + timedelta(7)).strftime("%Y-%m-%dT00:00:00Z")

r = calendar(MINTime=week_ago, MAXTime=week_later)
result = r.urlopen()
for i in range(0,len(result['items'])):
    print(result['items'][i]['summary'])