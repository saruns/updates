import sys
def revlook(x):
 d = dict()
 for f in x:
  if f not in d:
   d[f] = 1
  else:
   d[f] = d[f] + 1
 print "your dictionary is",d
 b = int(input("Enter your key-vlue: "))
 m = []
 n = []
 for i in d:
  if d[i] == b:
   m.append(i)
 if len(m) == 0:
  print n
 else:
  print m
a = raw_input("Enter your string: ")
revlook(a)
if __name__ == "__revlook__":
 revlook(a)
