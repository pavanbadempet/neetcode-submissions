class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
        heap = []
        for key,value in freq.items():
            if len(heap) < k:
                heapq.heappush(heap,(value,key))
            else:
                heapq.heappushpop(heap,(value,key))
        ans = [y for x,y in heap]
        return ans