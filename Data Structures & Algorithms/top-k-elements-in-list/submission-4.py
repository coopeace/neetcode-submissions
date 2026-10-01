class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        res = list()
        for n in nums:
            if counter.get(n,0) == 0:
                counter[n] = 1
            else:
                counter[n] += 1
        
        f = [ [value,key] for key,value in counter.items()]

        for i in range(k):
            max_value = max(f)
            res.append(max_value[1])
            f.remove(max_value)

        return res