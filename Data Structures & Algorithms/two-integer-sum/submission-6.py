class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myD = {}

        for i in range(len(nums)):
            num = nums[i]
            compt = target - num
            if compt in myD:
                return[myD[compt], i]

            myD[num] = i