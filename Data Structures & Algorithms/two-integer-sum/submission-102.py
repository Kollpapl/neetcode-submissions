class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mh = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mh:
                return [mh[diff], i]
            mh[n] = i
            
