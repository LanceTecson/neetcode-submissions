class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        arr = [0] * (target + 1)
        arr[0] = 1
        for i in range(len(arr)):
            for j in nums:
                if j > i:
                    break
                arr[i] += arr[i - j]
        return arr[-1]