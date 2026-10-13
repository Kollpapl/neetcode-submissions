class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        zet = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in zet:
                return[zet[diff], i]
            zet[n] = i