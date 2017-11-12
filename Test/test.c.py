import sys
class base1:
 def fun(self):
  print "hello, base1"
class derived1(base1):
 def fun2(self):
  print "hello, derived1"
a = derived1()
a.fun()
a.fun2()
