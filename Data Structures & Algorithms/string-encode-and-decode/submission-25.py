class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s
    def decode(self, s: str) -> List[str]:
        strs = []
        start = 0
        l = 0
        while l<len(s):
            while l<len(s) and s[l]!="#":
                l += 1
            length = int(s[start:l])
            w_s = l + 1
            w_e = w_s + length
            strs.append(s[w_s:w_e])
            start = l = w_e
        return strs