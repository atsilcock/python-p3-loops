#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i -= 1
        print("Happy New Year!")

# Yes, using a for loop is a good choice for iterating through a list. You'll want to 
# loop through each element of the list, apply the operation to square it, and then 
# collect these squared values.
# Finally, ensure that you return the list containing the squared values.

def square_integers(int_list):
    result = []
    for item in int_list:
        result.append(item ** 2)
    return result
    
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
    
