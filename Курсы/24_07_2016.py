#for i in range(5):
#   print i
    
import math
from time import time as t
a=2
b=5
c=2
#if a>b:
#    a,b=b,a
#while a<b:
#    print a
#    a+=c
d=b*b-4*a*c
if d<0:
    print d
    print "Net resheniya"
elif d==0:
    x=b/2*a
    print x
else: 
    x1=(-b+(math.sqrt(d)))/(2*a)
    x2=(-b-(math.sqrt(d)))/(2*a)
    print x1 , x2
    
    
r=range(2,10)
for i in r:
    for j in r:
        print i,"x",j,"=",i*j
        print "{} * {} = {}".format(i,j,i*j)
    print "\n"


f=range(100000)

y={}
t1=t()
for i in f:
   y[i]=''
t2=t()
#print y
print t2-t1
   
y=[]
t1=t()
for i in f:
   y.append(i)
t2=t()
#print y
print t2-t1,"wtf?"   