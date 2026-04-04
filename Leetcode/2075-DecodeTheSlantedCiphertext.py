class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Initialize list to store decoded characters
        result = []
      
        # Calculate number of columns in the matrix
        cols = len(encodedText) // rows
      
        # Iterate through each starting column position
        for start_col in range(cols):
            # Initialize position for diagonal traversal
            row_pos = 0
            col_pos = start_col
          
            # Traverse diagonally from current starting column
            while row_pos < rows and col_pos < cols:
                # Convert 2D position to 1D index and append character
                index = row_pos * cols + col_pos
                result.append(encodedText[index])
              
                # Move diagonally down-right
                row_pos += 1
                col_pos += 1
      
        # Join characters and remove trailing spaces
        return ''.join(result).rstrip()
