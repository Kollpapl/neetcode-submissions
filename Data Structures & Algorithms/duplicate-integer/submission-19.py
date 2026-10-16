class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pl = set()
        for n in nums:
            if n in pl:
                return True
            pl.add(n)
        return False    
      