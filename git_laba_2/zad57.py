import datetime


class Zate:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_weekday(self):
        return self.date.weekday()

    def get_weekday_name(self):
        weekdays = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        weekdayindex = self.date.weekday()
        return weekdays[weekdayindex]

    def get_month_name(self):
        months = '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
        monthindex = self.date.month
        return months[monthindex]


zate = Zate(2023, 6, 13)

print(zate.get_year())
print(zate.get_month())
print(zate.get_day())
print(zate.get_weekday())
print(zate.get_weekday_name())
print(zate.get_month_name())