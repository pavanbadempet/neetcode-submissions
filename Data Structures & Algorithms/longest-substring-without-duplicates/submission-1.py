class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        se = set()
        l = 0
        r = 0
        while r<len(s):
            while s[r] in se:
                se.remove(s[l])
                l += 1
            se.add(s[r])
            r += 1
            maxi = max(maxi,r-l)
        return maxi