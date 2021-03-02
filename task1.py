#!python3
'''
def sum(a,b):
    #inputs
    # a : float 
    # b : float
    # return value: returns the sum of the 2 numbers



#this should return a value of 7
x = sum(3,4)

#this should return a value of 12.5
y = sum(11,1.5)
'''

def largest( myList ):
    max = myList[ 0 ]
    for a in myList:
        if a > max:
            max = a
    return max