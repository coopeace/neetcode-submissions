class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list()
        suffix = list()

        accumlator = 1
        for n in nums:
            prefix.append(accumlator)
            accumlator *= n

        accumlator=1
        for n in reversed(nums):
            suffix.append(accumlator)
            accumlator *= n
        suffix.reverse()

        product = [prefix[i]*suffix[i] for i in range(len(nums))]

        return product