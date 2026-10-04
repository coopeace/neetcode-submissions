class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        warmer = [0]*n
        high = [[n-1,temperatures[n-1]]]
        for i in range(len(temperatures)-2,-1,-1):
            found=False
            while not found:
                if temperatures[i]>=high[-1][1]:
                    # print("higher:",high)
                    high.pop()
                    if not high:
                        warmer[i]=0
                        found=True
                        high.append([i,temperatures[i]])
                else:
                    # print("i:",temperatures[i],"j:",temperatures[i+1])
                    found=True
                    warmer[i]=high[-1][0]-i
                    # print("warmer:",warmer[i])
                    high.append([i,temperatures[i]])
                    # print("higher:",high)
        return warmer
