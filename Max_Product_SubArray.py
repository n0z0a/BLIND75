'''
Given an int array nums, find subarray that has
the largest product, and return the product
EX: 
nums = [2,3,-2,4]
Output: 6
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = 1
        cur_max = 1
        for num in nums:
            if num == 0:
                cur_min, cur_max = 1,1
                continue
            temp = num * cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(temp, num * cur_min, num)
            res = max(res, cur_max)
        return res
        