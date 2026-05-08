class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ["*", "+", "/", "-"]
        stk = []  
        # sum = 0 

    
        for token in tokens:
            if token in operators:
                match token:
                    case "+":
                        stk.append((stk.pop() + stk.pop()))
                    case "-":
                        v1, v2 = stk.pop(), stk.pop()
                        stk.append((v2 - v1))
                    case "*":
                        stk.append((stk.pop() * stk.pop()))
                    case "/":
                        v1, v2 = stk.pop(), stk.pop()
                        stk.append(int(float(v2) / v1))
            else:           
                stk.append(int(token))


        return stk[0]