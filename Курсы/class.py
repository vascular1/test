class P():
    a=10
    def __init__(self,x=0):
        self.x=x
    def m(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        # return self.x+other.x
        return P(self.x+other.x)
    def __str__(self):
        return "<Point x={}>".format(self.x)
    def __repr__(self):
        return "<Point x={}>".format(self.x)    
class Point():
    a=10
    b=0
    c=0
    def __init__(self,a=0,b=0,c=0):
        self.x=a
        self.y=b
        self.z=c
        
    def m(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c
    def __add__(self,other):
        # return self.x+other.x
        return Point(self.a+other.a,self.b+other.b,self.c+other.c)
    def __repr__(self):
        return "<Point x={}>".format(self.x)  
        
b=Point(2,4,8)    

print b


    
p=P()
print p.a
p.a*=2
print p.a
p.b=8
print p.b+p.a
p2=P()
print p2.a
print p2.__dict__
print p2.a
p2.a=5
print p2.__dict__
p3=P(5)
print p3.x
print p3.__dict__

p3.m(1,2)

print p3.a,p3.b,P.a


p4=P(10)
p5=P(20)
print p4+p5+p3
print p4.__add__(p5)
print p5.__add__(p4)
print [p4,p5]

print b