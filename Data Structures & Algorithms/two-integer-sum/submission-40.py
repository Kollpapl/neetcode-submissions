class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        merk = {}
        for k, l in enumerate(nums):
            diff = target - l
            if diff in merk:
                return[merk[diff], k]
            merk[l] = k
