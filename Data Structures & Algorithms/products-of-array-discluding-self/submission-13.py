class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        prefix = 1
        suffix = 1
        left = 0
        right = n - 1
        while left != n and right != -1:
            res[left] *= prefix
            res[right] *= suffix
            prefix *= nums[left]
            suffix *= nums[right]
            left += 1
            right -=1

        return res
