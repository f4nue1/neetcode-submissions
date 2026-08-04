class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        myLi = []
        myBool = True
        while myBool:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                myLi.append(left+1)
                myLi.append(right+1)
                myBool = False
        return myLi