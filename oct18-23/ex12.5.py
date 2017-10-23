import sys
def swap(x):
 b = []
 d = {}
 for f in open(x):
  b.append(f.strip())
 for f in b:
  t = list(f)
  t.sort()
  t = ''.join(t)
  if t not in d:
   d[t] = [f]
  else:
   d[t].append(f)
 for w in d.values():
  c = []
  for m in w:
   if m not in c:
    for n in w:
     count = 0
     e = []
     zip(m,n)
     for p,q in zip(m,n):
      if p != q:
       count = count + 1
     if count == 2:
      c.append(n)
      e.append((m,n))
      print e
swap("ex12.5.txt")
if __name__ == "__swap__":
 swap("ex12.5.txt")

