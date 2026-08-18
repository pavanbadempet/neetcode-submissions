class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = {}
        tc = {}
        for i in range(len(s)):
            sc[s[i]] = 1 + sc.get(s[i],0)
            tc[t[i]] = 1 + tc.get(t[i],0)
        return sc == tc