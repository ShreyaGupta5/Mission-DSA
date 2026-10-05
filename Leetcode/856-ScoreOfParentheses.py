class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Initialize total score and current depth level
        total_score = 0
        depth = 0
      
        # Iterate through each character with its index
        for index, char in enumerate(s):
            if char == '(':
                # Opening parenthesis increases nesting depth
                depth += 1
            else:  # char == ')'
                # Closing parenthesis decreases nesting depth
                depth -= 1
              
                # Check if this closing parenthesis forms "()" pattern
                if s[index - 1] == '(':
                    # A "()" at depth d contributes 2^d to the score
                    # Using bit shift: 1 << depth is equivalent to 2^depth
                    total_score += 1 << depth
      
        return total_score
