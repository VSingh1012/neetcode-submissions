class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # initialize the hash maps

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        n = len(board)


        for r in range(n):
            for c in range(n):
                value = board[r][c]
                sq_index = (r // 3) * 3 + (c // 3)
                if value != ".":
                    if value in rows[r] or value in cols[c] or value in squares[sq_index]:
                        return False
                    rows[r].add(value)
                    cols[c].add(value)
                    squares[sq_index].add(value)

                
        return True

                
                    

                




