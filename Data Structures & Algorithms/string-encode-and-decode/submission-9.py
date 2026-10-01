class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        return ":#".join(strs) 

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split(':#')

if __name__ == "__main__":
    strs = ["Hello","World"]
    s = Solution().encode(strs)
    print(Solution().decode(s))
