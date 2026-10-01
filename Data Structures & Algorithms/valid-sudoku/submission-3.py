class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        boxes = {(i,j):set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                pointer = board[r][c]
                
                # skip "."
                if pointer == ".":
                    continue

                # check for rows duplicates
                if pointer in rows[r]:
                    return False
                else:
                    rows[r].add(pointer)

                # check for cols duplicates
                if pointer in cols[c]:
                    return False
                else:
                    cols[c].add(pointer)

                # check for boxes duplicates
                box_coordinate = (r//3,c//3)
                if pointer in boxes[box_coordinate]:
                    return False
                else:
                    boxes[box_coordinate].add(pointer)
        return True
       