class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = s + str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        l = 0
        while l<len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            strs.append(s[r+1:r+1+length])
            l = r+1+length
        return strs