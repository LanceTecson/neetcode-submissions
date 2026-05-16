class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def cond(m):
            cap, d = m, 1
            for i in weights:
                while cap - i < 0:
                    d += 1
                    if d > days:
                        return False
                    cap = m
                cap -= i
            return True

        l, r = 1, sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if cond(m):
                r = m
            else:
                l = m + 1
        return l