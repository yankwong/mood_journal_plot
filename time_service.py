import datetime


class TimeService:

    def get_timestamp(self, time_string: str) -> float:
        element = datetime.datetime.strptime(time_string, "%m/%d/%Y")
        return datetime.datetime.timestamp(element)

    def get_string_from_timestamp(self, time_stamp: float) -> str:
        return datetime.datetime.utcfromtimestamp(time_stamp).strftime("%m/%d/%Y")
