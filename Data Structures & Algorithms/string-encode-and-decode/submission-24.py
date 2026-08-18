class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += str(len(w)) + '#' + w
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        l = 0
        while l<len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            start = r+1
            end = start+length
            strs.append(s[start:end])
            l = end
        return strs