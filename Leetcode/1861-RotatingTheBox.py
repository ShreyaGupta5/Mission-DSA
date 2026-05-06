class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m = len(box)
        n = len(box[0])
        
        # 1. Apply Gravity: Move stones ('#') to the right for each row
        for row in box:
            empty_spot = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    empty_spot = col - 1
                elif row[col] == '#':
                    row[col], row[empty_spot] = '.', '#'
                    empty_spot -= 1
                    
        # 2. Rotate 90 degrees clockwise
        # Original (r, c) becomes (c, m - 1 - r)
        res = [['.' for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = box[r][c]
                
        return res
