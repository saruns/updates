import sys
def get(x):
 d = dict()
 for f in x:
  count = d.get(f,0)
  count = count + 1
  d[f] = count 
 return d
a = raw_input("Enter your string:  ")
b = list(a)
print get(b)
if __name__ == "__get__":
 get(a)
