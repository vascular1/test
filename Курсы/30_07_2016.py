l=[1,2,1,3,2]
n=[]
h=[]
for i in l:
    
    if not i in n:
        n.append(i)
print n


#def foo():
#        a,b=10,20
#        c=a+b
#        print c
    
#for i in range(2):    
#    foo()    

#def foo(a,b):
#        print a+b
        
#foo(2,4)        
#foo(5,6)
#for k in range(10):
#    foo(k,k+1)


def foo(a,b):
    return a+b
    
print foo(2,5)    

def ku(n):
    return n+n
print ku(2)    
print ku("privet")
print foo("la","la")