class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for n in nums:
            if counter.get(n,0) == 0:
                counter[n] = 1
            else:
                counter[n] += 1
        f = [ [value,key] for key,value in counter.items()]
        f.sort(reverse=True)
        s = f[:k]
        return [s[i][1] for i in range(len(s))]
