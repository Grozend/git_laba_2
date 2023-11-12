import datetime


class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_seconds_difference(self):
        difference = self.end - self.start
        return difference.total_seconds()

    def get_minutes_difference(self):
        seconds = self.get_seconds_difference()
        minutes = seconds // 60
        return minutes

    def get_hours_difference(self):
        minutes = self.get_minutes_difference()
        hours = minutes // 60
        return hours

    def get_days_difference(self):
        hours = self.get_hours_difference()
        days = hours // 24
        return days


start = datetime.datetime(2023, 3, 1, 0, 56)
end = datetime.datetime(2023, 3, 2, 7, 34)
period = Period(start, end)

print(period.get_seconds_difference())
print(period.get_minutes_difference())
print(period.get_hours_difference())
print(period.get_days_difference())
