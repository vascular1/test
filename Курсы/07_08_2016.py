# -*- coding: utf-8 -*-
s = "380500000000"
code=["050","039","067"]


if s[0]=="+":
    s=s[1:]
    print s
if s[0]=="3":
    s=s[1:]
    print s
if s[0]=="8":
    s=s[1:]
    print s
if s[:3] in code:
    print "okey",s[:3]
    
    
#039 xxx xx xx - Киевстар (Golden Telecom)
#050 xxx xx xx - МТС
#063 xxx xx xx - life:)
#066 xxx xx xx - МТС
#067 xxx xx xx - Киевстар
#068 xxx xx xx - Киевстар (Beeline)
#091 xxx xx xx - Utel
#092 xxx xx xx - PEOPLEnet
#093 xxx xx xx - life:)
#094 xxx xx xx - Интертелеком
#095 xxx xx xx - МТС
#096 xxx xx xx - Киевстар
#097 xxx xx xx - Киевстар
    
    
    

d=len(s)    
if 12==d:
    
    print "ok",s
else:
    print "not ok"
n=3
l=range(3)
it=iter(l)
try: 
    str(0)/1
    print it.next()
    print it.next()
    print it.next()
    print it.next()
    print it.next()
#except StopIteration:
#    pass
except Exception,why:
    print why,type(why).__name__
#    print why.__dict__
#    print dir(why)
    print why.message,why.args
def gen():
    yield 0
    yield 1
    yield 2
g=gen()  
print g.next()
for i in g:
    print i
    
def gen1(n):
    i=0
    while i!=n:
        yield i
        i+=1
        
g1=gen1(5)  
print g1.next()
for i in g1:
    print i    
    
    
def gen2(n,i):
    while i!=n:
        yield n
        n+=1  
     
    
g2=gen2(2,5)  
#print g2.next()
#for i in g2:
#    print i    
print list(g2)    
            
def gen3(n,i,y):
    while i!=n:
        yield n
        n+=y  
g3=gen3(2,20,2)      

print list(g3)

