class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        res = list()
        for n in nums:
            if counter.get(n,0) == 0:
                counter[n] = 1
            else:
                counter[n] += 1
        
        f = list(set(counter.values()))
        f.sort(reverse=True)
        t = 0
        duplicate = counter.copy()
        for i in f:
            if t == k:
                return res
            for key,value in counter.items():
                val = duplicate.get(key,0)
                if val == i and val != 0:
                    res.append(key)
                    duplicate.pop(key)
                    t+=1

        return res

