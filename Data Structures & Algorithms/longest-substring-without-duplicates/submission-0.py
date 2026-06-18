class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        hashMap = {}
        for R, c in enumerate(s):
            if c in hashMap and hashMap[c] >= L:
                L = hashMap[c] + 1
            
            hashMap[c] = R
            length = max(length, R-L + 1)
        return length
        
        
                

            
        