class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left,right = 0, len(height) -1
        leftMax = 0
        rightMax = 0
        while left < right:
            if leftMax < height[left]:
                leftMax = height[left]
            if rightMax < height[right]:
                rightMax = height[right]
            if leftMax < rightMax:
                res += leftMax - height[left]
            else :
                res += rightMax - height[right]
            if leftMax < rightMax:
                left+=1
            else :
                right-=1
        return res
