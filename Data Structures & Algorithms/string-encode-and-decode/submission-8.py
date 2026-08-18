class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + str(len(i)) + '#' + i
        return s
    def decode(self, s: str) -> List[str]:
        ans = []
        l = 0
        while l<len(s):
            j = l
            while s[j]!='#':
                j+=1
            length = int(s[l:j])
            l = j+1
            r = l+length
            ans.append(s[l:r])
            l = r
        return ans
