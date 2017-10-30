import sys
import os
def walk(x,m):
 b = os.listdir(x)
 c = []
 for f in b:
  d = os.path.join(x,f)
  if os.path.isfile(d):
   if d.endswith(m):
    c.append(d)
  else:
   c.extend(walk(d,m))
 return c
a = raw_input("Enter your directory name: ")
m = raw_input("Enter your suffix: ")
print walk(a,m)
if __name__ == "__walk__":
 walk(a)
