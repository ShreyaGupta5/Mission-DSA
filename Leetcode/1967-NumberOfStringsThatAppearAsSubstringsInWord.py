class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        # Initialize counter for matching patterns
        count = 0
      
        # Iterate through each pattern in the list
        for pattern in patterns:
            # Check if current pattern is a substring of word
            if pattern in word:
                count += 1
      
        return count
