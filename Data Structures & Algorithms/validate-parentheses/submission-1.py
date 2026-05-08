class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairMap = {"}" : "{",
                    ")" : "(",
                    "]" : "["}

        for c in s:
            if c in pairMap:
                if stack and stack[-1] == pairMap[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False

        