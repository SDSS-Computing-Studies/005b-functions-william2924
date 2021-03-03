#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInterger(number):
    # input: a float number
    # return: Ture if the number is an integer
    # return: False, if the number is not an integer
    if number == int(number):
        return True
    else:
        return False
# This should return False
x = isInterger( 9.5 )
# This should return Ture
y =( -2 )