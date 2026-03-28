from typing import List
from string import ascii_lowercase

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
      
        n = len(lcp)
      
        # Initialize result string array with empty strings
        result_string = [""] * n
      
        # Greedy assignment: assign smallest available character to unassigned positions
        current_position = 0
        for character in ascii_lowercase:
            # Find next unassigned position
            while current_position < n and result_string[current_position]:
                current_position += 1
          
            # All positions have been assigned
            if current_position == n:
                break
          
            # Assign current character to all positions that must have same character
            # based on LCP matrix (if lcp[i][j] > 0, positions i and j must share prefix)
            for j in range(current_position, n):
                if lcp[current_position][j] > 0:
                    result_string[j] = character
      
        # Check if all positions have been assigned
        if "" in result_string:
            return ""
      
        # Validate the constructed string against the LCP matrix
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if result_string[i] == result_string[j]:
                    # Characters match, so LCP should continue
                    if i == n - 1 or j == n - 1:
                        # At boundary: LCP should be exactly 1
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        # Not at boundary: LCP should be 1 + LCP of next positions
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
                else:
                    # Characters don't match, so LCP should be 0
                    if lcp[i][j] != 0:
                        return ""
      
        # Join the character array into final string
        return "".join(result_string)
