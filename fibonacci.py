a=0
b=1
d=str(a)+" "+str(b)+" "
for i in range(10):
  c=a+b
  d+=str(c)+" "
  a=b
  b=c
print(d)
