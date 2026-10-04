class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenn = {}
        for index, number in enumerate(nums):
            value = target - number
            if value in seenn:
                return [seenn[value], index] 
            seenn[number] = index
        