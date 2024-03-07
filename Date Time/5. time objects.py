from datetime import datetime
from datetime import timedelta
from datetime import time

"""
class relationship
object
    timedelta
    tzinfo
         timezone
    * time
    date
        datetime
"""

# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

t = time(12,45,28)
print("t = ", t)

# CLASS ATTRIBUTES
print()
print("CLASS ATTRIBUTES")
print()

print("time.min", time.min)
print("time.max", time.max)
print("time.resolution", time.resolution)


# INSTANCE ATTRIBUTES
print()
print("INSTANCE ATTRIBUTES")
print()

print("t.hour", t.hour)
print("t.minute", t.minute)
print("t.second", t.second)
print("t.microsecond", t.microsecond)
print("t.tzinfo", t.tzinfo)
print("t.fold", t.fold)


# SUPPORTED OPERATIONS
print()
print("SUPPORTED OPERATIONS")
print()

t1 = datetime.now().time()
t2 = time(22,00,00)
print("t1", t1)
print("t1>t2", t1>t2)

# INSTANCE OPERATIONS

print()
print("INSTAMCE OPERATIONS")
print()


t3 = t2.replace(hour = 21)
print("t3", t3)


print("isoformat(auto) ", t2.isoformat(timespec='auto'))
print("isoformat(hours) ", t2.isoformat(timespec='hours'))
print("isoformat(minutes) ", t2.isoformat(timespec='minutes'))
print("isoformat(seconds) ", t2.isoformat(timespec='seconds'))
print("isoformat(milliseconds) ", t2.isoformat(timespec='milliseconds'))
print("isoformat(microseconds) ", t2.isoformat(timespec='microseconds'))

print("time.__str__()", t2.__str__())
print("time.strftime(format)", t2.strftime("%H .. %M ..  %S"))









