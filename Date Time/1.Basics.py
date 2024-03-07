"""
# there are twi kind fo date time object
   naive: does not have enough information to represent an unambiguous moment 
          in time (for instance does not distinguish between UTC and local time
   aware: knows about algorithms and political time adjustments, it is used to 
          specify a specific and unambiguous moment in time. For instance is 
          able to distinguish between local time and UTC

   
"""

import datetime

print("Min Year",datetime.MINYEAR)
print("Max year", datetime.MAXYEAR)

#DATE TIME TYPES AVAILABLE
#naive

# datetime: assumes that the gregorian calendar as been is and will be
# always valid

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









