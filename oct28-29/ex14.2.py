def sed(m,n,o,p):
 try:
  fin = open(o, 'r')
  fout = open(p, 'w')
  for f in fin:
   line = f.replace(m, n)
   fout.write(line) 
  fin.close()
  fout.close()
 except:
  print "Somethig wrong"
a = raw_input("Enter your pattern: ")
b = raw_input("Enter your replacement string: ")
c = raw_input("Enter your source file: ")
d = raw_input("Enter your dest file: ")
sed(a,b,c,d)
if __name__ == "__sed__":
 sed(a,b,c,d) 
