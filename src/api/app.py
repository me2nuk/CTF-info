from datetime import datetime, timedelta
import requests
from .config import *

global_url = "https://www.googleapis.com/calendar/v3/calendars/%s/events?orderBy=startTime&singleEvents=true&timeMin={}&timeMax={}&key=%s"% (calendars_Id, auth_key)

class calendar:
    def __init__(self, MINTime, MAXTime) -> None:
        self.MINTime = MINTime
        self.MAXTime = MAXTime
        self.url = global_url.format(self.MINTime, self.MAXTime)

    def urlopen(self) -> dict:
        calendar_urlOpens = requests.get(self.url)
        return calendar_urlOpens.json()