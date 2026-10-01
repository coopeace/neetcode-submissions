class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = list()
        counter = dict()
        for n in nums:
            if counter.get(n,0) == 0:
                counter[n] = 1
            else:
                counter[n] += 1

        buckets = [ [] for i in range(len(nums)+1)]

        for key,count in counter.items():
            buckets[count].append(key)

        for i in range(len(buckets)-1,-1,-1):
            for item in buckets[i]:
                res.append(item)
                if len(res) == k:
                    return res
        return []

