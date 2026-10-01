class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                sum = nums[i] + nums[j+1]
                if sum == target and i != j+1:
                    res =[i,j+1]
        res.sort()
        return res
