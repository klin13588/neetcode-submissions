class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for c in s:
          if c.isalnum():
            cleaned += c.lower()

        L, R = 0, len(cleaned) - 1

        while L < R:
          if s[L] == s[R]:
            L += 1
            R -= 1
          else:
            return False
        return True