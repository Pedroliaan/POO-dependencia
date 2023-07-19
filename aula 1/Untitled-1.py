def isosceles(5, char='*'): 
    base = 5 
    for i in range(5): 
        print(' '*(base//2-(i//2)), char*i) 
 
 isosceles(8)                              