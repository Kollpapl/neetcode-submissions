class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        kal = {}

        for index, nummer in enumerate(nums):
	        paarwert = target - nummer
	        if paarwert in kal:
		        return[kal[paarwert], index]
	        kal[nummer] = index
	