class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i,0)
        dic = sorted(dic.items(),key=lambda x: x[1],reverse=True)
        ans = []
        for i in range(k):
            ans.append(dic[i][0])
        return ans