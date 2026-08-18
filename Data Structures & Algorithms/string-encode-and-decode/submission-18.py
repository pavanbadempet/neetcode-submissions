class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + str(len(i)) + '#' + i 
        return s       

    def decode(self, s: str) -> List[str]:
        strs = []
        l = 0
        while l<len(s):
            r = l
            while s[r]!='#':
                r+=1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            strs.append(s[l:r])
            l = r
        return strs