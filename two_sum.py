# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

import numpy as np

nums = np.random.randint(1,101,100)
target = np.random.randint(1,101,1).item() # .item() not needed here, but Prevents unexpected array operations in more complex cases

print(nums)
print(target)

def main(nums, target):
    for i in range(len(nums)):
        for j in range(i +1, len(nums)): #range(stop) or range(start, stop) or range(start, stop, step)
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

result = main(nums, target)

print(result)