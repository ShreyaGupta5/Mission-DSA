class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0      # Previous group size
        curr = 1      # Current group size
        result = 0    # Final answer
        
        for i in range(1, len(s)):
            
            if s[i] == s[i - 1]:
                curr += 1   # Same character → increase group size
            else:
                result += min(prev, curr)  # Add valid substrings
                prev = curr   # Move current to previous
                curr = 1      # Reset current group
        
        result += min(prev, curr)  # Add last group
        
        return result
