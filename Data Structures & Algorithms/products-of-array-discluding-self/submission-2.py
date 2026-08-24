class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1
        for x in nums:
            if x!=0:
                total *= x
        for x in nums:
            if x == 0:
                zeros += 1
        if zeros >1:
            return [0]*len(nums)
        elif zeros == 1:
            return [total if x==0 else 0 for x in nums]
        ans = []
        for n in nums:
            ans.append((total//n))
        return ans
