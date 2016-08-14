#def index_power(array, n):
#    """
#        Find Nth power of the element with index N.
#    """
#    if (len(array)>n):
#        return pow(array[n], n)
#    else:
#        return -1

#if __name__ == '__main__':
#    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
#    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
#    assert index_power([0, 1], 0) == 1, "Zero power"
#    assert index_power([1, 2], 3) == -1, "IndexError"

def checkio(array):
    print array
    b=[]
    c=array
#    for n in range(len(array)):
#        number=n
#        if number % 2 == 0:
#            #print number
#            a.append(number)
#    b=len(array)
#    print b-1
#    print a
#    print sum(a)*(b-1)
    k=range(0,len(c),2)
    print array
    
    #for n in k:
        
        
    
    return array
    
  
    

print checkio([1, 3, 5])

#These "asserts" using only for self-checking and not necessary for auto-testing
#if __name__ == '__main__':
#    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#    assert checkio([6]) == 36, "(6)*6=36"
#    assert checkio([]) == 0, "An empty array = 0"