# -*- coding: utf-8 -*-
def my(n):
    while n!=1:
        if n%2:
            n=3*n+1
            
        else:
            n=n/2
        print n
    


print my(10)

s="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
a=0
c=0
g=0
t=0
b=[]
for n in s:
    if n=="A":
        a=a+1
       
    if n=="C":
        c=c+1
       
    if n=="G":
        g=g+1
       
    if n=="T":
        t=t+1
print a,"_",c,"_",g,"_",t
print s.count("A"),s.count("C")

s="GATGGAACTTGACTACGTAAATT"
print s.replace("T","U")

s="AAAACCCGGT"
s1=[]
for n in s:
    if n=="A":
        s1.append("T")
    if n=="C":
        s1.append("G")
    if n=="T":
        s1.append("A") 
    if n=="G":
        s1.append("C")    
print s


    
