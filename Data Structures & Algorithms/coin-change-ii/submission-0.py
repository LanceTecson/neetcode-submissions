class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ret = [0] * (amount + 1)
        ret[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                ret[j] += ret[j - i]
        return ret[-1]