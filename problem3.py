#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""


def factor(number):
    mylist = []
    number = 37
    print(" The factors of " + str(number) + " are ", end=" ")
    for whole_number in range(1,number + 1):
        if number % whole_number == 0:
            mylist.append(whole_number)
            print(mylist)


def factors(x):
   print("The factors of",x,"are:",end=" ")
   for i in range(1, x + 1):
       if x % i == 0:
           mylist.append(i)
           print(mylist)
           

mylist = []

num = 12
factors(num)

num = 37
factors(num)