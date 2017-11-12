import math
import sys
def sin(x):
 t = 0
 k = 50
 for i in range(k):
  m = x**(2*i+1)
  p = math.factorial(2*i+1)
  if 1 % 2 == 0:
   t = t + m/p
  else:
   t = t - m/p
 return t
a = float(input("Enter the num: "))
print sin(a)
if __name__ == "__sin__":
 sin(a)

