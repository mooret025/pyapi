#!/usr/bin/env python3

import datetime as dt

my_object = dt.datetime.now()
my_other_object = dt.datetime.now().isoformat()
another_time_obj = dt.datetime.date(my_object)
back2future = dt.datetime(1955, 11, 5, 9, 45, 50)
back2future2 = dt.datetime.timetuple(back2future)
back2futureplus1 = back2future + dt.timedelta(1)



print(my_object)
print()
print(my_other_object)
print()
print(another_time_obj)
print()
print(back2future)
print()
print(back2future2)
print()
print(back2futureplus1)


