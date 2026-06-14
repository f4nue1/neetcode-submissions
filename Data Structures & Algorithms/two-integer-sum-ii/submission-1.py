class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myList = []
        for i in range(len(numbers)):
            for j in range(1, len(numbers)):
                if numbers[i] + numbers[j] == target and  i < j:
                    myList.append(i + 1)
                    myList.append(j + 1)
                    break
        return myList
