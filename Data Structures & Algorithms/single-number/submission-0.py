class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        y = 0
        for i in range(len(nums)):
            x = nums.count(nums[i])
            if x == 1:
               y = nums[i]
            
        return y
