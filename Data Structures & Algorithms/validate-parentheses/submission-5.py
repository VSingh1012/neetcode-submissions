class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stk = []
              

        for c in s:
            if c in valid_map:
                if stk and stk[-1] == valid_map[c]:
                    stk.pop() # pops if the highest open brace on the stack == current character's mapped open brace (since it is closed brace)
                else:
                    return False

            else:
                stk.append(c) # appends the open parentheses            
            
            



        return True if not stk else False
                
                    
    
        
        
        