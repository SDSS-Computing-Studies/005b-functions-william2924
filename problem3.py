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
def factors(number):
    list = []
    print("factors ("+ str(number) +") == ",end = "")
    for whole_number in range(1,number + 1):
        if number % whole_number == 0:
           list.append(whole_number)
    print(list)