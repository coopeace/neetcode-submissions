class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in consecutive:
                count = 1 
                while n+1 in consecutive:
                    count += 1
                    n += 1
                if count > longest:
                    longest = count

        return longest

