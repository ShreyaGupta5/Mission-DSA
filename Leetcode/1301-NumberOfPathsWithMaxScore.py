class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        def update_cell(curr_row: int, curr_col: int, prev_row: int, prev_col: int) -> None:
            
            # Skip if previous cell is out of bounds or unreachable
            if prev_row >= board_size or prev_col >= board_size or max_score[prev_row][prev_col] == -1:
                return
          
            # Skip if current cell is obstacle or start position
            if board[curr_row][curr_col] in "XS":
                return
          
            # If previous cell has better score, update current cell
            if max_score[prev_row][prev_col] > max_score[curr_row][curr_col]:
                max_score[curr_row][curr_col] = max_score[prev_row][prev_col]
                path_count[curr_row][curr_col] = path_count[prev_row][prev_col]
            # If previous cell has same score, add its path count to current
            elif max_score[prev_row][prev_col] == max_score[curr_row][curr_col]:
                path_count[curr_row][curr_col] += path_count[prev_row][prev_col]
      
        board_size = len(board)
      
        # max_score[i][j] stores the maximum score to reach cell (i, j)
        max_score = [[-1] * board_size for _ in range(board_size)]
      
        # path_count[i][j] stores the number of paths with maximum score to reach cell (i, j)
        path_count = [[0] * board_size for _ in range(board_size)]
      
        # Initialize the end position 'S' at bottom-right corner
        max_score[-1][-1] = 0
        path_count[-1][-1] = 1
      
        # Process cells from bottom-right to top-left
        for row in range(board_size - 1, -1, -1):
            for col in range(board_size - 1, -1, -1):
                # Update current cell from three possible previous cells
                update_cell(row, col, row + 1, col)      # Cell below
                update_cell(row, col, row, col + 1)      # Cell to the right
                update_cell(row, col, row + 1, col + 1)  # Cell diagonally down-right
              
                # Add the score of current cell if it's reachable and contains a digit
                if max_score[row][col] != -1 and board[row][col].isdigit():
                    max_score[row][col] += int(board[row][col])
      
        MOD = 10**9 + 7
      
        # Return result for start position 'E' at top-left corner
        if max_score[0][0] == -1:
            return [0, 0]
        else:
            return [max_score[0][0], path_count[0][0] % MOD]
