import re


class Date:
    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MINUTES_YEAR = 525600
    MINUTES_LEAP_YEAR = MINUTES_YEAR + 1440

    def __init__(self, year: str, month: str, day: str):
        self.year = year
        self.month = month
        self.day = day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        PATTERN = r"^(\d{2}){1,2}$"
        try:
            assert re.match(PATTERN, year)
            assert int(year) > 1900 and int(year) <= 2032

            self._year = year
        except AssertionError:
            raise ValueError("invalid year format")
        except:
            raise ValueError("uncaught error has occured")

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        try:
            assert int(month) >= 1 and int(month) <= 12

            self._month = month
        except AssertionError:
            raise ValueError("invalid month format")
        except:
            raise ValueError("uncaught error has occured")

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        try:
            assert int(day) >= 1 and int(day) <= 31

            self._day = day
        except AssertionError:
            raise ValueError("invalid day format")
        except:
            raise ValueError("uncaught error has occured")

    # @classmethod
    # def isleap(cls, year):
    #     y = int(year)
    #     if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    #         return True
    #     else:
    #         return False

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    def __sub__(self, other):
        #self - other
        year = int(self.year)
        month = int(self.month)
        day = int(self.day)
        days_offset = 0

        otheryear = int(other.year)
        othermonth = int(other.month)
        otherday = int(other.day)
        other_days_offset = 0

        total_minutes = 0

        if year < otheryear:
            raise ValueError("can't be subtracted")

        for y in range(otheryear, year):
            if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
                total_minutes += Date.MINUTES_YEAR
            else:
                total_minutes += Date.MINUTES_LEAP_YEAR

        for m in range(1, month):
            if m == 2:
                if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                    days_offset += 28
                else:
                    days_offset += 29
            else:
                days_offset += Date.MONTHS[m-1]

        for m in range(1, othermonth):
            if m == 2:
                if otheryear % 4 != 0 or (otheryear % 100 == 0 and otheryear % 400 != 0):
                    other_days_offset += 28
                else:
                    other_days_offset += 29
            else:
                other_days_offset += Date.MONTHS[m-1]

        days_offset += day
        other_days_offset += otherday

        total_offset = (days_offset - other_days_offset) * 24 * 60
        print(total_offset)
        print(total_minutes)
        total_minutes += total_offset
        print(f"{total_minutes:,}")


date = Date("2008", "02", "25")
date2 = Date("2009", "11", "1")
(date2 - date)
