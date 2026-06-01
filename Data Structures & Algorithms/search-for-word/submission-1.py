class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # exists = False
        num_cols = len(board[0])
        num_rows = len(board)
        visited = set()


        def dfs(r, c, i, seen):
            if i == len(word):
                return True

            if (r < 0 or r >= num_rows or c < 0 or c >= num_cols) or (r,c) in seen or board[r][c] != word[i]:
                return False

            seen.add((r, c))

            res = (dfs(r + 1, c, i + 1, seen) or dfs(r - 1, c, i + 1, seen) or dfs(r, c + 1, i + 1, seen) or dfs(r, c - 1, i + 1, seen))
            # erase your changes
            seen.remove((r, c))

            return res


        for r in range(num_rows):
            for c in range(num_cols):
                if dfs(r, c, 0, visited):
                    return True

        return False
            
    


            

                
