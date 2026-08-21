class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                # not a number
                if board[i][j] == ".":
                    continue
                # row logic 
                if i in rows:
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].append(board[i][j])
                else:
                    rows[i] = [board[i][j]]
                # column logic (same as row but with j)
                if j in cols:
                    if board[i][j] in cols[j]:
                        return False
                    else:
                        cols[j].append(board[i][j])
                else:
                    cols[j] = [board[i][j]]
                # square logic 
                si = i // 3
                sj = j // 3
                if (si,sj) in squares:
                    if board[i][j] in squares[(si,sj)]:
                        return False
                    else:
                        squares[(si,sj)].append(board[i][j])
                else:
                    squares[(si,sj)] = [board[i][j]]

        return True

                    
       
        