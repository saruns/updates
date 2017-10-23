import sys
def words(x):
 d = {}
 for f in x:
  if f not in d:
   d[f] = 1
  else:
   d[f] = d[f] + 1
 print d 
 b = []
 for m in d:
  b.append((str(d[m]),str(m)))
 print b
 b.sort(reverse = True)
 c = []
 for p,q in b:
  c.append(q)
 return c
a = raw_input("Enter the string: ")
print words(a)
if __name__ == "__words__":
 words(a)
