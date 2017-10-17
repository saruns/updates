import sys
def rotate(x):
 d = {}
 for f in x:
   for i in range(1,10):
    p = f[-i:] + f[:-i]
    if p != f:
     if p in x:
      d[f] = p 
      print d,"rotated by",i
      d = {}
b = []
for f in open('rotate.txt'):
 c = f.strip().lower()
 b.append(c)
rotate(b)
if __name__ == "__rotate__":
 rotate(b)
