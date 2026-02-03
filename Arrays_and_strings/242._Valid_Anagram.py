class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq={}
        freq1={}
        for x in s: 
            freq[x]=freq.get(x,0)+1 
        for y in t:
            freq1[y]=freq1.get(y,0)+1
        if freq != freq1:
            return False 
        return True   
