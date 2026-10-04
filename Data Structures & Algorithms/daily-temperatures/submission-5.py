class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        warmer = [0]*n
        high = [[n-1,temperatures[n-1]]]
        for i in range(len(temperatures)-2,-1,-1):
            while high and temperatures[i]>=high[-1][1]:
                high.pop()
            if high:
                warmer[i]=high[-1][0]-i
            high.append([i,temperatures[i]])
        return warmer
     