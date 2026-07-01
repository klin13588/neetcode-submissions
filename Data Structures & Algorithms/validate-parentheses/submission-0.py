class Solution:
    def isValid(self, s: str) -> bool:
         x = list(s)
         
         if len(x) % 2 == 1:
            return False
        