class Solution:
    def isValid(self, s: str) -> bool:

  

        map_valid = {
            "}" : "{", 
            "]" : "[", 
            ")" : "("
        }

        stk = []
        
        # stk: [

        for c in s:
            if c in map_valid.values(): # 
                stk.append(c)
            else:
                if stk:
                    if map_valid[c] == stk[-1]:
                        stk.pop()
                    else:
                        return False
                else: 
                    return False
                
            
        return True if not stk else False