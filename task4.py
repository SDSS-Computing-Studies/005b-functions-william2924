#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
def isInteger( number):
    # input: a float number
    # return: True if the number is an integer
    # return: False,if the number is not a integer
    if number==int(number):
        return True
    else:
        return False
# This should return Flase
x = isInteger(9.5)
# This should be return True
y = (-2)