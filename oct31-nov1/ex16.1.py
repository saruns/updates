import sys
def time_day(x):
 print "%2d:%2d:%2d" % (p.hour,p.minutes,p.seconds)
class time(object):
 "time"
def hour(h):
 count = 1
 for f in range(13,25):
  if h == f:
   z = count
  else:
   count = count + 1
 return z
a = int(input("Enter your hour: "))
b = int(input("Enter your minutes: "))
c = int(input("Enter your seconds: "))
p = time()
if a > 12:
 hour(a)
 p.hour = hour(a)
else:
 p.hour = a
p.minutes = b
p.seconds = c
time_day(p)
