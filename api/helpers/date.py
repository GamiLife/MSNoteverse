from datetime import datetime,timedelta

import pytz


class DateHelper:
    date_str: str
    date: datetime

    def __init__(self,date=""):
        if date != "":
            self.date = datetime.fromisoformat(date)

    def str(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    def tz(self,timezone="America/Lima"):
        time_zone = pytz.timezone(timezone)
        self.date = self.date.replace(tzinfo=pytz.utc).astimezone(time_zone)
        return self

    def add(self, minutes=0, seconds=0):
        self.date = self.date + timedelta(minutes=minutes,seconds=seconds)
        return self

    def now(self):
        time_zone = pytz.timezone("America/Lima")
        now = datetime.now(time_zone)
        self.date = now
        return self

    '''
        Get difference between date stored and input date.
        @:return { expired, mm, ss, hh, dd }
    '''

    def diff(self,date_compare: datetime):
        diff_result = self.date - date_compare

        dd = diff_result.days
        hh = (diff_result.seconds / 60) / 24
        mm = diff_result.seconds / 60
        ss = diff_result.seconds

        response = {"invalid":  date_compare > self.date,"dd": int(dd),"hh": int(hh),"mm": int(mm),"ss": int(ss)}
        return response
