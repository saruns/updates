import sys
def move_rect(m,n,o):
 p.corner.x = p.corner.x + n
 p.corner.y = p.corner.y + o
 print p.corner.x
 print p.corner.y
 return m
class rect(object):
 "rectangle"
p = rect()
p.width = 100.0
p.height = 60.0
p.corner = rect()
p.corner.x = 0.0
p.corner.y = 3.0
a = int(input("Enter the no to increment the x_cordinate: "))
b = int(input("Enter the no to incrememt the y_cordinate: "))
print move_rect(rect,a,b)
if __name__ == "__move_rect__":
 move_rect(rect,a,b)
