class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(position[i],speed[i]) for i in range(len(position))]
        pair = sorted(pair,key=lambda x : x[0],reverse=True)
        time = [(target-p[0])/p[1] for p in pair]
        fleet = 0
        prev_time = 0
        for t in time:
            if t > prev_time:
                fleet+=1
                prev_time=t
        return fleet

