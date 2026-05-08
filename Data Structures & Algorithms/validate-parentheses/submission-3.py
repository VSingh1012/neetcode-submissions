class Solution:
    def isValid(self, s: str) -> bool:
        stackk = []
        closeMap = {
            ")" : "(", "]" : "[", "}" : "{"
        }

        for c in s:
            if c in closeMap:
                if stackk and stackk[-1] == closeMap[c]:
                    stackk.pop()
                else:
                    return False
                
            else: 
                stackk.append(c)
            

        return True if not stackk else False
        