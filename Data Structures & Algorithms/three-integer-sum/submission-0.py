class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if (i != 0 and nums[i] == nums[i-1]) or (nums[i]>0):
                continue
            l = i + 1
            r = n - 1
            while l<r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif curr > 0:
                    r -= 1
                else:
                    l += 1
        return ans