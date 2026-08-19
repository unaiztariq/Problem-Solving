"""__________________________________________________________________________________________"""
# Q5: Write a Python program that prints all numbers from 1 to 100. However, for multiples of 3, print "Fizz,"
#  for multiples of 5, print "Buzz," and for multiples of both, print "FizzBuzz."
"""__________________________________________________________________________________________"""

def fizzbuzz():
    for i in range (1,101):
        if i%3 ==0 and i %5 ==0:
            print("fizzBuzz")
        elif i%3 ==0 :
            print("fizz")
        elif  i %5 ==0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
