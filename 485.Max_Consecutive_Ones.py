class Solution(object):
    def findMaxConsecutiveOnes(self,nums):        
        temp = []
        n = 0 
        for i in range(len(nums)):                      
            if nums[i] == 1:
                temp += [nums[i]]
                if len(temp) > n:
                    n = len(temp)
            else:          
                temp = []
                continue
        return n
