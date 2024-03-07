"""
class relationship
object
    * timedelta
    tzinfo
        timezone
    time
    date
        datetime
"""

# TIMEDELTA OBJECTS
# represent a duration, a difference between two dates or times
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

from datetime import timedelta

d = timedelta(1,0,0,0,30,12,0)
print(d)

t1 = timedelta(hours=2.5)
t2 = timedelta(minutes=30)
print("t1= ", t1)
print("t2= ",t2)
# t1 + t2
print("t1 + t2 = ", (t1 + t2))
# t1 - t2
print("t1 - t2 = ", (t1 - t2))
# t2 - t1
print("t2 - t1 = ", (t2 - t1))
# t1 * 2
print("t1*2 = ", (t1 * 2))
# t1/t2
print("t1/t2 = ",t1/t2 )
i = 3
f = 3.5
# t1//i integer part of the division
print("i= ", i)
print("f = ", f)
print("t1/i = ", t1/i)
print("t1/f = ", t1/f)

# t1%t2  reminder of the division
t3 = timedelta(hours=1)
print(t3)
print("t1 % i = ", t1 % t3)
t4 = timedelta(hours=-1)
print("t4= ", t4)
print("abs(t4)", abs(t4))
print("str(t1)", str(t1))
print("repr(t1)", repr(t1))


# calculating how many periods are within a higher one

periods = dict()
periods["H4"] = timedelta(hours=4)
periods["H1"] = timedelta(hours=1)
periods["m30"] = timedelta(minutes=30)
periods["m15"] = timedelta(minutes=15)
periods["m5"] = timedelta(minutes=5)
periods["m1"] = timedelta(minutes=1)

print("H1 within H4 = ", periods["H4"]/periods["H1"])
print("m15 within H4 = ", periods["H4"]/periods["m15"])

