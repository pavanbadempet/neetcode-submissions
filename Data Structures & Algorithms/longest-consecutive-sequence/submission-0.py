class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                cnt = 1
                while num+cnt in nums:
                    cnt += 1
                longest = max(longest,cnt)
        return longest
