def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def has_duplicate(arr):
            new_arr = list()
            for text in arr:
                if text != '.': new_arr.append(text)
            if len(new_arr) == 0: return False
            if len(set(new_arr)) != len(new_arr):
                return True 
            return False
        
        # horizontal check 
        for line in board: 
            if has_duplicate(line): 
                return False 
            
        # vertical check 
        for col in range(9):
            check_col_arr = list()
            for row in range(9):
                check_col_arr.append(board[row][col])
            if has_duplicate(check_col_arr):
                return False 
        
        # 3x3 square check 
        i, j = 0, 0 
        while i < 10:
            while j < 9: 
                check_col_arr = list()
                for col in range(i, i+3):
                    for row in range(j, j+3):
                        check_col_arr.append(board[col][row])
                if has_duplicate(check_col_arr): return False 
                j += 3
            j = 0 
            i += 3 
        return True
