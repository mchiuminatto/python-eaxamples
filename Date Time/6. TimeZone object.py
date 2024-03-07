from datetime import datetime
from datetime import timedelta
from datetime import time
from datetime import timezone

"""
class relationship
object
    timedelta
    tzinfo
         timezone
     time
    date
        datetime
"""

# class datetime.timezone(offset, name=None)

tzo1 = timezone(offset=timedelta(hours=-1))
tzo2 = timezone(name=)

print(tzo1.__str__())
print(tzo2.__str__())
