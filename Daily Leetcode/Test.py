nums = [0, 1, 2, 0, 3]

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)
            print(nums)
        else:
            continue
        return nums

moveZeroes(nums)