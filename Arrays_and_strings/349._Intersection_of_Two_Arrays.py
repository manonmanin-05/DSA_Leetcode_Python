class Solution(object):
    def intersection(self, nums1, nums2):
        output=[]
        freq={}
        for x in nums1:
            freq[x]=freq.get(x,0)+1
        for x,y in freq.items():
            if x in nums2:
                output.append(x)
        return output   
