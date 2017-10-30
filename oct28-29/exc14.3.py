import sys
import shelve
def anagram(x,y,z):
 for m,n in y.iteritems():
  x[m] = n
 x.close()
 x = shelve.open('anagram1.db')
 q = list(z)
 q.sort()
 q = ''.join(q)
 try:
  print x[q]
 except:
  print "some error"
d = {}
b = []
a = raw_input("Enter your filenme:  ")
fin = open(a, 'r')
for f in fin:
 b.append(f.strip())
for i in b:
 t = list(i)
 t.sort()
 t = ''.join(t)
 if t not in d:
  d[t] = [i]
 else:
  d[t].append(i)
c = shelve.open('anagram1.db', 'c')
e = raw_input("Enter your string: ")
anagram(c,d,e)
if __name__ == "__anagram__":
 anagram(c,d,e)
