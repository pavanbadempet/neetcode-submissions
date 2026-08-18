class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            alpha = [0]*26
            for c in word:
                alpha[ord(c)-ord('a')] += 1
            ans[tuple(alpha)].append(word)
        return ans.values()