import sys
class Complex:
 def __init__(self,real,imag):
  self.real=real
  self.imag=imag
 def __str__(self):
  return str(self.real) + '+i' + str(self.imag)
 def add(self, other):
  c=Complex(self.real + other.real,self.imag + other.imag)
  return c
 def multi(self, other):
  d=Complex(self.real*other.real - self.imag*other.imag,self.imag*other.real + self.real*other.imag)
  return d
a=Complex(1,2)
b=Complex(3,4)
c=a.add(b)
d=a.multi(b)
print c
print d
