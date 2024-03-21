class Solution(object):
    def isValidSudoku(self, board):
        my_set = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                r = str(board[i][j]) + "row" + str(i)
                c = str(board[i][j]) + "col" + str(j)
                b = str(board[i][j]) + "box" + str(i // 3) + "_" + str(j // 3)
                if r in my_set or c in my_set or b in my_set:
                    return False
                my_set.add(r)
                my_set.add(c)
                my_set.add(b)
        return True
