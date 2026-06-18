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
        
        dictS = {}
        dictT = {}

        for c in s:
            dictS[c] = dictS.get(c, 0) + 1

        for c in t:
            dictT[c] = dictT.get(c, 0) + 1
        
        if dictT == dictS:
            return True
        else:
            return False
