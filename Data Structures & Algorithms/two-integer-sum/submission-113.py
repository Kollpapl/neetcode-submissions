class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        fick = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in fick:
                return [fick[diff], i]
            else:
                fick[n] = i  
            
