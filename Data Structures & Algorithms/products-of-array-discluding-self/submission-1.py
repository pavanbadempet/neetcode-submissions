class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        length = len(nums)
        ans = [0] * length
        for i in nums:
            if i == 0:
                zeros += 1
        if zeros>1:
            return ans
        prod = 1
        for i in nums:
            if i!=0:
                prod *= i
        if zeros == 1:
            for i in range(length):
                if nums[i] == 0:
                    ans[i] = prod
                    return ans
        else:
            for i in range(length):
                ans[i] = prod//nums[i]
            return ans
            
