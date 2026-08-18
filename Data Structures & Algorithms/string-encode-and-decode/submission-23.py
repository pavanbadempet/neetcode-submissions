class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = s + str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            strs.append(s[start:end])
            i = end
        return strs