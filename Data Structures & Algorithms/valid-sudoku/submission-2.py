class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        create an array, each item is a set representing an entry 
        - rows, cols, boxes (use mathematical trick) 
        check if current number already in item set 

        """

        set_rows = [set() for _ in range(0,9)]
        set_cols = [set() for _ in range(0,9)]
        set_box = [set() for _ in range(0,9)]


        for i in range(0,9): 
            for j in range(0,9):
                curr = board[i][j]
                if curr == ".":
                    continue
                box = (i // 3) * 3 + (j // 3) #what box is the row, what box is the column, *3 so we know what box leads to 
                if curr in set_rows[i] or curr in set_cols[j] or curr in set_box[box]:
                    return False
                else: 
                    set_rows[i].add(curr)
                    set_cols[j].add(curr)
                    set_box[box].add(curr)

        return True
