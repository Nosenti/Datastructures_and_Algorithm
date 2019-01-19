
nums = [1, 2, 3, 4]
target = 3
new = []
def twoSum():

    i = 0
    while (i < len(nums)):
        j = 0
        while (j < len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return new.extend([i, j])
            j += 1
        i += 1


print(twoSum())