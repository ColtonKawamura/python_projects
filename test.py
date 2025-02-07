nums = [1,2,5,1,2]

def main(nums):
    seen_nums = []
    for num in nums:
        if num in seen_nums:
            seen_nums.remove(num)
        else:
            seen_nums.append(num)
    return seen_nums.pop()

print(main(nums))