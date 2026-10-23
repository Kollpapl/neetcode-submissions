class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        senn = {}

        for i, n in enumerate(nums):
            diff = target - n

            if n in senn:
                return[senn[n], i]

            senn[diff] = i
