import sys
import os
def walk(x):
 b = os.listdir(x)
 for f in b:
  c = os.path.join(x,f)
  if os.path.isfile(c):
   print c
  else:
   walk(c)
a = raw_input("Enter your directory name: ")
walk(a)
if __name__ == "__walk__":
 walk(a)
