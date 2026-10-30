class Solution:
    def isValid(self, s: str) -> bool:
        opposite_bracket = {"(": ")", "[": "]", "{": "}"}

        stack = []

        for c in s:
            if c in opposite_bracket: #guckt nur auf key
                stack.append(c)
            else:
                if not stack:
                    return False
                selected = stack.pop() #was war das element das gepoppt wurde?
                if opposite_bracket[selected] != c: #schlag nach was ist der key UND was ist der wert?, 
                #da steht also "}" != "}" sprich: anstatt nur selected zu schreiben wollen wir das opposit
                    return False
        return not stack

