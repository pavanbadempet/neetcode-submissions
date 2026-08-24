class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            pre[i] *= post
            post *= nums[i]
        return pre