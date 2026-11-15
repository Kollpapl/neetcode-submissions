class Solution:
    def isValid(self, s: str) -> bool:
        mh = {")": "(", "]": "[", "}": "{"}

        stack = []

        for c in s:
            if c in mh:
                if stack and stack[-1] == mh[c]:
                    stack.pop()
                else:
                    return False                    
            else:
                stack.append(c)
        
        return True if not stack else False   
