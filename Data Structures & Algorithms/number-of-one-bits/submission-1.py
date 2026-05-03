class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            ret += 1 & n
            n >>= 1
        return ret