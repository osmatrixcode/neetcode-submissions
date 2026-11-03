class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        create set for rows, columns, squares
        loop through each number (r,c) 

        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9): 
            for c in range(9): 
                num = board[r][c]
                if num == ".": 
                    continue
                box = (r // 3) * 3 + (c // 3) #calculate what 'sector it is in 
                if num in rows[r] or num in cols[c] or num in squares[box]: 
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[box].add(num)

        return True