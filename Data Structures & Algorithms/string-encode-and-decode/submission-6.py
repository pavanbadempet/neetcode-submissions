class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans = ans + str(len(i)) + '#' + i
        return ans
            
    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l<len(s):
            r = l
            while s[r]!='#':
                r+=1
            lg = int(s[l:r])
            l = r + 1
            r = l + lg
            res.append(s[l:r])
            l = r
        return res
