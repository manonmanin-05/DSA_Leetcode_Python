class Solution(object):
    def containsDuplicate(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for x in freq.values():
            if x >=2:
                return True
                continue
        return False 
 
        
