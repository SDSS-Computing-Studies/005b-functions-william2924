#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(myList):
    max = myList[0]
    for a in myList:
        if a > max:
            max = a
    return max