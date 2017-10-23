import sys
def anagram(x):
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
  print w
anagram('anagram.txt')
if __name__ == "__anagram__":
 anagram('anagram.txt')
