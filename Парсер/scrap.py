recent_presidents=['fack','shet','nax']
print 'Preziki  %s.' % ', '.join(recent_presidents)    
print recent_presidents


squares = map(lambda a: a*a, [1,2,3,4,5])   
print squares
squares = map(lambda a: a*a*a, [1,2,3,4,5])
print squares

add2 = ["a","b","c"]
print  'Preziki  %s.' % ', '.join(add2),add2

numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    squares.append(number*number)
    print numbers,"___",number,"_____",squares
print squares,"___",numbers  
    
numbers = [1,2,3,4,5]
numbers = map(lambda x: x*x, numbers)
print "___",numbers,"___",squares,"_____"

numbers = [1,2,3,4,5]
squares = [number+number+number for number in numbers]
print "___",numbers,"____",squares


numbers = [1,2,3,4,5]
numbers_under_4 = [1]
for number in numbers:
    if number < 4:
        numbers_under_4.append(number)
        print numbers,numbers_under_4        

numbers = [1,2,3,4,5]
numbers_under_4 = filter(lambda x: x < 4, numbers)  
print numbers_under_4

numbers = [1,2,3,4,5]
numbers_under_4 = [number for number in numbers if number > 2]
print numbers_under_4


numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    if number < 4:
        squares.append(number*number)
        print squares 
print squares        

numbers = [1,2,3,4,5]
squares = [number*number for number in numbers if number < 4]
print squares


numbers = (1,2,3,4,5) 
squares_under_10 = (number*number for number in numbers if number*number < 10)


for square in squares_under_10:
    print square


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
mygenerator=createGenerator()
print mygenerator
for i in mygenerator:
    print i
    
    
    