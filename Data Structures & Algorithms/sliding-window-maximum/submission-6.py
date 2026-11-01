class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        l = 0
        res = list()
        for r in range(len(nums)):
            while d and nums[d[-1]]<nums[r]:
                d.pop()
            
            d.append(r)

            if r - l + 1 == k :
                res.append(nums[d[0]])
                if d[0]==l:
                    d.popleft()
                l+=1
        return res
