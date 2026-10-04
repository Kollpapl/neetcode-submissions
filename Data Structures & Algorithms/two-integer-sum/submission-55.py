class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        senn = {}
        for index, number in enumerate(nums):
            val = target - number
            if val in senn:
                return [senn[val],index]
            senn[number] = index
