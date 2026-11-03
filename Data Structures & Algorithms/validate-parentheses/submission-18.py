class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {"{": "}", "(": ")", "[": "]"}
        
        stack = []

        for c in s:
            if c in opposite:
                stack.append(c)
            else:
                if not stack:
                    return False
                else: 
                    key = stack.pop()
                    if opposite[key] != c:
                        return False
        if stack:
            return False
        else:
            return True
