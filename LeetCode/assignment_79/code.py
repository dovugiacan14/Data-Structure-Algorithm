def word_search(board, word):
    if not board or not board[0]:
        return False 
    
    rows = len(board)
    cols = len(board[0])
    word_len = len(word)

    def backtrack(row, col, index): 
        if index == word_len:
            return True 
        
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
            return False  

        temp, board[row][col] = board[row][col], "#"

        found = (
            backtrack(row + 1, col, index+1) or
            backtrack(row - 1, col, index + 1) or
            backtrack(row, col + 1, index + 1) or
            backtrack(row, col - 1 , index + 1) 
        ) 
        board[row][col] = temp 
        return found 

    for i in range(rows): 
        for j in range(cols):
            if board[i][j] == word[0] and backtrack(i, j, 0): 
                return True 
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(word_search(board, word))
