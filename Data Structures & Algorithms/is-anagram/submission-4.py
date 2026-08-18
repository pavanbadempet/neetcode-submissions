class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sb = [0] * 26
        tb = [0] * 26
        for i in range(len(s)):
            sb[ord(s[i])-ord('a')] += 1
            tb[ord(t[i])-ord('a')] += 1
        return sb==tb