class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # variation of the valid parenthesis problem

        open_stk = []

        n = len(s)
        for x in range(n):
            if s[x] == "(":
                open_stk.append(x)
            elif s[x] == ")":
                if open_stk and s[open_stk[-1]] == "(":
                    open_stk.pop()
                else:
                    open_stk.append(x)


        # second loop to find all the invalid characters
        open_stk = set(open_stk) #for the O(1) lookup

        new_str = ""

        for x in range(n):
            if x not in open_stk:
                new_str += s[x]


        return new_str


                








        