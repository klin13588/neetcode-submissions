class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        L = 0
        best = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[L])
            best = max(best, R-L + 1)
        return best