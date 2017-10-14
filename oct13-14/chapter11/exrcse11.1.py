import sys
def dictfile(x):
 c = []
 b = dict()
 index = 1
 for f in open(x):
  c.append(f)
 for s in c:
  b[index] = s  
  index = index + 1
 print b
dictfile('output.txt')
if __name__ == "__dictfile__":
 dictfile('output.txt')
