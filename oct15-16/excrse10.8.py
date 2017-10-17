import sys
def list_dup(x):
 y = []
 count = 0
 for f in x:
  if f not in y:
   y.append(f)
  else:
   count = count + 1
 if count > 0:
  print "True"
  print "element is repeating"
 else:
  print "False"
  print "no element is repeating"
print "enter your element"
a = raw_input()
b = list(a)
list_dup(b)
if __name__ == "__list_dup__":
 list_dup(b)
