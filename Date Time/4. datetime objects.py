from datetime import datetime
from datetime import timedelta
from datetime import time

"""
class relationship
object
    timedelta
    tzinfo
        * timezone
    time
    date
        datetime
"""

# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

# CLASS METHODS
print("CLASS METHODS")
print()
print("datetime.today() ", datetime.today())
print("datetime.utcnow() ", datetime.utcnow())
print("datetime.now(t) ", datetime.now())
print("datetime.fromtimestamp(timestamp, tz=None)", datetime.fromtimestamp(1000000000))
print("datetime.utcfromtimestamp(timestamp)", datetime.utcfromtimestamp(1000000000))
print("datetime.fromordinal(ordinal)", datetime.fromordinal(200))
d1 = datetime(2017,7,1)
t1 = time(12,1,1)
print("d1 = " + d1.__str__(), "t1 =" + t1.__str__())
print("datetime.combine(date, time, tzinfo=self.tzinfo)", datetime.combine(d1, t1))
date_string = "7/3/2017 08:30"
print("string date ", date_string)
print("datetime.strptime(date_string, format)", datetime.strptime(date_string, "%m/%d/%Y %H:%M"))
print()
print()


# CLASS ATTRIBUTES
print("CLASS ATRIBUTES")
print()
print("datetime.min", datetime.min)
print("datetime.max", datetime.max)
print("datetime.resolution", datetime.resolution)

print()
print("INSTANCE ATTRIBUTES")
print()
# INSTANCE ATTRIBUTES
d = datetime(2017, 7, 3, 11, 00)
print("date ", d)
print("datetime.year", d.year)
print("datetime.month", d.month)
print("datetime.day", d.day)
print("datetime.hour", d.hour)
print("datetime.minute", d.minute)
print("datetime.second", d.second)
print("datetime.microsecond", d.microsecond)
print("datetime.tzinfo", d.tzinfo)
print("datetime.fold", d.fold)

print()
print("OPERATIONS")
print()

d1 = datetime(2017, 6, 19, 12, 30, 00)
d2 = datetime(2017, 6, 20, 13, 45, 00)
t1 = timedelta(hours=50)

print("d1", d1)
print("d2", d2)
print("t1", t1)

print("d1+t1", d1+t1)
print("d1-t1", d1-t1)
print("d1-d2", d1-d2)
print("d1 > d1", d1 > d2)

# INSTANCE METHODS
print()
print("INSTANCE METHODS")
print()

print("datetime.date()", d1.date())
print("datetime.time()", d1.time())
print("datetime.timetz()", d1.timetz())
print("d1 before replacing", d1)
print("datetime.replace()", d1.replace(year=2016))
print("datetime.astimezone()", d1.astimezone())

# as we haven't seen yet the time zone objects all this methods
# needs to be taste

print("datetime.utcoffset()", d1.utcoffset())
print("datetime.dst()", d1.dst())
print("datetime.tzname()", d1.tzname())
print("datetime.utctimetuple()", d1.utctimetuple())

# OTHER METHODS
print("datetime.weekday()", d1.weekday())
print("datetime.isoweekday()", d1.isoweekday())
print("datetime.isocalendar()", d1.isocalendar())
print("datetime.isoformat()", d1.isoformat(sep='t'))
print("datetime.ctime()", d1.ctime())

