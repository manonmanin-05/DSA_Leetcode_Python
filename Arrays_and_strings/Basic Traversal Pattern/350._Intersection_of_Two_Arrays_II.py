class Solution(object):
    def intersect(self, nums1, nums2):
        output=[]
        freq={}
        freq1={}
        count=0
        for x in nums1:
            freq[x]=freq.get(x,0)+1
        for x in nums2:
            freq1[x]=freq1.get(x,0)+1
        for x in freq:
            if x  in freq1:
                count = min(freq[x], freq1[x])
                for i in range(count):
                    output.append(x)        
                        
        return output
