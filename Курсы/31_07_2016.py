#https://checkio.org/
#https://www.codewars.com/
#https://ru.khanacademy.org/
#https://ide.c9.io/tolearn/ruby
foo=lambda a,b:a+b
print foo(10,20)
fooKub=lambda a:a*a*a
print fooKub(10)

print foo
print (lambda x:x**3)(10)

def foo(n):
    def foo2(m):
        return n+m
    return foo2       
f=foo(100)
print f(1),f(2),f(200)
    
print foo,foo(2),foo(2)(3) 

r=round
def my(foo,n):
    return foo(n)
print my(r,2.5)
print r(1.2)

def my2(a,b,n=2):
    return a+b+n
print my2(1,2),my2(1,2,3)

def my3(a,b,n=2,m=3):
    return a+b+n
print my3(1,2),my3(1,2,m=10,n=30)    

def my4(*a):
    return sum(a)
    
#    print (*a)
print my4(*[1,2,3])
print sum([1,2,3])
print my4(),my4(1),my4(*range(10))

def my5(*a):
    a=list(a)
    a[0]+=10
    return sum(a)*2
print my5(2,3,1,22)   

def d(f):
    def w(*a):
        print a
        rez=f(*a)
        print rez
        return rez
    return w
my2=d(my2) 
print my2(1,2)
