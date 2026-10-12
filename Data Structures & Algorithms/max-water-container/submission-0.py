class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        c_area = 0
        l,r = 0,len(heights)-1
        while l < r:
            if heights[l] < heights[r]:
                c_area = heights[l]*(r-l)
            else :
                c_area = heights[r]*(r-l)
            if c_area > max_area:
                max_area = c_area
            if heights[l] < heights[r]:
                l+=1
            else :
                r-=1
        return max_area