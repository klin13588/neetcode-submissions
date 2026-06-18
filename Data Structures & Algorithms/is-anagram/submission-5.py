class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        first we must check if they are the same length if not return false

        create two dicts
        dictS
        dictT 

        loop through both 

        then do a final loop through both dicts and compare values 
        
        '''

        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}

        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i],0) + 1
            dictT[t[i]] = dictT.get(t[i],0) + 1
        
        return dictS == dictT
