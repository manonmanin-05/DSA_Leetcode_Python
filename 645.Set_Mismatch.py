class Solution(object):
    def findErrorNums(self, nums):
        missing_val=0
        duplicate=0
        temp=[]
        s=set()
        for i in range(1,len(nums)+1):
            if i not in nums:                
                missing_val=i               
        for i in nums:
            if i in s: 
                duplicate=i
            else:
                s.add(i)
        temp=duplicate,missing_val
        return temp
