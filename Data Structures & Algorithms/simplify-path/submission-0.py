class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stk = []
        file_names = path.split('/')
        # files_and_dirs = ["neetcode", "practice", "/", "...", "//", "..", "courses"]
        # stk: [neetcode, practice, ]
        forbidden_chars = {"", ".", ".."}
        n = len(file_names)
        i = 0 

        while i < n:
            # conditional popping + incrementing of the i pointer
            while stk and i < n and file_names[i] == "..":
                stk.pop()
                i += 1

            if i < n and file_names[i] not in forbidden_chars:
                stk.append(file_names[i])
            i += 1

        return ("/" + "/".join(stk)) if stk else "/"

        



            

        







