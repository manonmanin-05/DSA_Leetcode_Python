class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        output=[]
        count=0
        for i in nums:
            for j in nums:
                if j < i:
                    count+=1                   
            output.append(count) 
            count=0             
        return output
                
