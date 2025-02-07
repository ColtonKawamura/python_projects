# Given an array of integers nums and an integer k, find the maximum value in each sliding window of size k as the window moves from left to right.

# Need to create a random array of integers

import numpy as np

def random_array(size, min_val, max_val):
    return np.random.randint(min_val, max_val, size).tolist() # use NumPy's "random" module function "randint" to create a random. Use tolist() is a heuristic for speed efficieny.

nums = random_array(10, 1, 10)
print(nums)
k = np.random.randint(1,3,1)
print(k)

# Next, I know that it will be a funciton that will take "nums" and "k" as an input and return "max_value". Let's just create some action in it to test it.

def mainV1(nums,k):
    max_value = max(nums)
    print(max_value)
    return max_value

mainV1(nums,k)

# Let's build up on it. 
def mainV2(nums, k):
    
    for i = range(len(nums)):
        
    return max_value