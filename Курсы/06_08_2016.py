

def cube(x):
    return x**3
m= map(lambda m:m**3,range(5))
print (list(m))
print (lambda m:m**3)(5)
l=[]
for i in range(5):
    l.append(i**3)
print l    
print [i**3 for i in range(5)]  

print (lambda i:i**3)(5)

print [(lambda x:x**3)(i) for i in range(5)]



def odd(x):
    return   x%2
print filter(odd,range(5))

for i in range(5):
    if odd(i):
        l.append(cube(i))
print l    


print map(cube,(filter(odd,range(5))))
print map(lambda x:x**3,filter(lambda x: x%2, range(5)))
print [i**3 for i in range(5) if i%2]
print reduce(lambda x,y:x+y,range(5))

def sum(i,j,k):
    return i+j+k
print sum(*[1,2,3])
print apply(sum,[1,2,3])

def apply2(foo,*a):
    return foo(*a)
