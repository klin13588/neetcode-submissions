class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        newStr = list(newStr)

        l,r = 0, len(newStr)-1

        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True 