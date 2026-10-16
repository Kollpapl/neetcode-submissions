class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dcit = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dcit:
                return [dcit[diff], i]
            dcit[n] = i
