#!/usr/bin/env python3

# Write a function happy_new_year() using a while loop that outputs numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"

def happy_new_year(num=10):
    while num >= 1:
        print(num)
        num -= 1
    print("Happy New Year!")
    


# Write a function square_integers() that takes one argument, a list of integers and returns the list of squared elements.

def square_integers(int_list):
    return [num**2 for num in int_list]
    

# Write a function fizzbuzz() that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".



def fizzbuzz():
    for number in range(1,101):
        if number%3 == 0 and number%5 ==0:
            print("FizzBuzz")
        elif number%3 == 0:
            print("Fizz")
        elif number%5 == 0:
            print("Buzz")
        else:
            print(number)
        
    