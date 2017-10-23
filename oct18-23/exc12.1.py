import sys
def sum_all(x):
 c = 0
 for f in x:
  c = c + f
 print "The sum is",c
n = int(input("Enter the no of elements: "))
a = [0 for i in range(n)]
print "Enter te elements: "
for i in range(n):
 a[i] = input()
b = tuple(a)
sum_all(b)
if __name__ == "__sum_all__":
 sum_all(b)
