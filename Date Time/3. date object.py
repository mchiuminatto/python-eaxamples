from datetime import date
from datetime import timedelta

"""
class relationship
object
    timedelta
    tzinfo
        timezone
    time
    *date
        datetime
"""

# representation of a date in an idealized calendar
# class datetime.date(year, month, day)

#class methods

print("today = ", date.today())
print("date (from ordinal) = ", date.fromordinal(737000))
print("date (from timestamp) = ", date.fromtimestamp(737000))

d = date(2017, 1, 1)

print("date", d)
print("year", d.year)

#OPERATIONS

d1 = date(2017,6,14)
d2 = date(2016,6,1)
t1 = timedelta(days=60)

print("d1 = ", d1, "d2 = ", d2, "delta = ", t1)

# d1 - t1
print("d1 - t1 = ", d1- t1)
print("d1 + t1 = ", d1+ t1)

# d1 - d2
print("d1 - d2", d1 - d2)

# error
try:
    d4 = date(2017, 13, 1)
except BaseException as e:
    print(e.args)

#booelan operations

print(d1 > d2)

# INSTANCE METHODS

print("d1.timetuple() =", d1.timetuple())
print("day of the year", d1.timetuple().tm_yday)
d1.replace(month=7)  # didin't worked
print(d1)
print("day of the year", d1.timetuple().tm_yday)

print("ordinal ", d1.toordinal())
print("weekday ", d1.weekday())
print("weekday iso ", d1.isoweekday())
print("iso calendar ", d1.isocalendar())
print("iso format ", d1.isoformat())
print("c time ", d1.ctime())





