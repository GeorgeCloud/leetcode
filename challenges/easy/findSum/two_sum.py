# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(self, nums, target):
    """
    nums   <---- set of numbers    (list)
    target <---- number to be find (integer)
    output ---> [array of two values that make target]
    """
    numbers = {}
    for index, value in enumerate(nums):
        if target - value in numbers:
            return [numbers[target - value], index]
        numbers[value] = index
