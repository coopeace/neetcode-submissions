class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()
        for n in nums:
            if n in track:
                return True
            else :
                track.add(n)
        return False
