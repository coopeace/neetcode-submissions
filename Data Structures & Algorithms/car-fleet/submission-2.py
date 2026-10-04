class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(position[i],speed[i]) for i in range(len(position))]
        pair = sorted(pair,key=lambda x:x[0],reverse=True)
        fleet = list()
        for p in pair:
            time=(target-p[0])/p[1]
            fleet.append(time)
            if len(fleet)>1 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)

