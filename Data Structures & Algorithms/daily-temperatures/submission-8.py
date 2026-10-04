class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        warmer = [0]*n
        high = [n-1]
        for i in range(n-2,-1,-1):
            while high and temperatures[i]>=temperatures[high[-1]]:
                high.pop()
            if high:
                warmer[i]=high[-1]-i
            high.append(i)
        return warmer
       