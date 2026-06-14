class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myL = []
        myBool = False
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if(nums[i] + nums[j] == target) and (i != j):
                    myL.append(i)
                    myL.append(j)
                    myBool = True
            if(myBool):
                break
                    
                    
        return myL
