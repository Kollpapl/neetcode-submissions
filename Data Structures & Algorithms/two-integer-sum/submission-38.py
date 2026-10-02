class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        zettel = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in zettel:
                return [zettel[diff], i]
            zettel[n] = i