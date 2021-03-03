#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(a,b,c):
    #input: 
    #      a is a float number
    #      b is a float number
    #      c is boolean
    # hypotenuse = math.sqr(a*a+b*b)
    #return: the missing side
    if c == True:
        hypotenuse = math.sqrt(a*a+b*b)
        return hypotenuse
    else:
        list=[a,b]
        list.sort()
        hypotenuse = list[-1]
        c = math.sqrt((hypotenuse*hypotenuse)-(list[0]*list[0]))
        return c

# this should return a value of 5
hypotenuse(3,4,True)
# this should return a value of 12
hypotenuse(13,5,False)