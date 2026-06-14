class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       myArr = []
       for i in range(len(digits)):
            myArr.append(str(digits[i]))
       s = "".join(myArr)
       x = str(int(s) + 1)
       myR = []
       for i in range(len(x)):
         myR.append(int(x[i]))
       return myR
       
         