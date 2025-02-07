# Given a non-empty array of integers nums, where every element appears twice except for one, find that single number.

nums = [1,2,1,4,2]

def main(nums):
    seen = set() # not really needed, but set() only keep unique values
    print(seen)
    for num in nums:
        if num in seen:
            seen.remove(num)
            print(seen)
        else:
            seen.add(num)
    return seen.pop() # returns a random element from "seen"; there's only one so it "pop" the number we want

print(main(nums))