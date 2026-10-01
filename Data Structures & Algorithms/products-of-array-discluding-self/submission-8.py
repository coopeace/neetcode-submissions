class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        accumlator=1
        # prefix
        for i in range(len(nums)):
            res[i] = accumlator
            accumlator *= nums[i]

        accumlator=1
        # suffix
        for i in range(len(nums)-1,-1,-1):
            res[i] *= accumlator
            accumlator *= nums[i]

        return res
