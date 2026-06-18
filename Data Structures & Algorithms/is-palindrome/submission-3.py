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

        l, r = 0, len(newStr) - 1

        while r > l:
            if newStr[l] == newStr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True