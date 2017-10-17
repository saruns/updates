import sys
def dict_dup(x):
 d = {}
 for f in x:
  if f in d:
   return d[f]
  else:
   d[f] = 'True'
 return 'false'
n = int(input("Enter the limit of list: "))
print "Enter the elements: "
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input()
print dict_dup(a)
if __name__ == "__dict_dup__":
 dict_dup(a)
