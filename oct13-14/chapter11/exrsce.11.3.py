import sys
def sortdict(x):
 d = dict()
 for f in x:
  if f not in d:
   d[f] = 1
  else:
    d[f] = d[f] + 1
 b = sorted(d.keys())
 for w in b:
  print w, d[w]
a = raw_input("Enter your string: ")
sortdict(a)
if __name__ == "__sortdict__":
 sortdict(a)

