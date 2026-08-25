class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            a = [0]*26
            for c in word:
                a[ord(c)-ord('a')] += 1
            hashabale = tuple(a)
            if hashabale not in ans:
                ans[hashabale]= []
            ans[hashabale].append(word)
        return list(ans.values())