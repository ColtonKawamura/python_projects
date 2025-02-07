# The FizzBuzz question is a common coding interview problem that tests your ability to use loops and conditional statements efficiently

# The problem is as follows:
# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# ------------- Begin -------------------------------------
# First, let's write a function that does the first part of the problem, the build up from there.
def fizzBuzzV1():
    for i in range(1, 101): # range(start, stop, step) step is optional, so is "start" which default is start = 0
        print(i)

# Let's test the function
fizzBuzzV1()

# Next we will add the condition to print "Fizz" for multiples of 3
def fizzBuzzV2():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
            print(i) # just to make sure
            
fizzBuzzV2()


# Next, add a part for multipels of five
def fizzBuzzV3():
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
            print(i) # again, just checking for now

fizzBuzzV3()

# Now the final statement. Start with the most specific requirement to the least

def fizzBuzzV4():
    for i in range (1, 100):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 ==0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzzV4()
