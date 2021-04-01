from datetime import datetime, timedelta
import requests
from .config import *

global_url = "https://www.googleapis.com/calendar/v3/calendars/%s/events?orderBy=startTime&singleEvents=true&timeMin={}&timeMax={}&key=%s"% (calendars_Id, auth_key)
global_url_q = "https://www.googleapis.com/calendar/v3/calendars/%s/events?q={}&key=%s"% (calendars_Id, auth_key)
class calendar:
    def __init__(self, MINTime, MAXTime) -> None:
        self.MINTime = MINTime
        self.MAXTime = MAXTime
        self.url = global_url.format(self.MINTime, self.MAXTime)

    def urlopen(self) -> dict:
        print(self.url)
        calendar_urlOpens = requests.get(self.url, timeout=4)
        return calendar_urlOpens.json()

class calendar_Queries:
    def __init__(self, Search) -> None:
        self.Search = Search
        self.url = global_url_q.format(self.Search)

    def urlopen(self) -> dict:
        print(self.url)
        calendar_URLOpens = requests.get(self.url, timeout=4)
        return calendar_URLOpens.json()