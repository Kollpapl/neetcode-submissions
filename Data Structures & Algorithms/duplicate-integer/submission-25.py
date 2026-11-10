class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        stack = set()

        for i in nums:
            if i not in stack:
                stack.add(i)
            else: 
                return True
        return False