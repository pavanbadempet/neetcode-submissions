class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        for i in range(len(nums)):
            if i == len(nums):
                left = nums[:i]
                mul = 1
                for i in left:
                    mul *= i
                    prod.append(mul)
            else:
                leftandright = nums[:i] + nums[i+1:]
                mul = 1
                for i in leftandright:
                    mul *= i
                prod.append(mul)
        return prod
            
