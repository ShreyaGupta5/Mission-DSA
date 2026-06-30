class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Dictionary to track the most recent index of each character
        # Initialize with -1 to indicate characters haven't been seen yet
        last_seen_index = {"a": -1, "b": -1, "c": -1}
      
        # Counter for valid substrings
        total_count = 0
      
        # Iterate through the string with index and character
        for current_index, char in enumerate(s):
            # Update the most recent index for the current character
            last_seen_index[char] = current_index
          
            # Find the minimum index among all three characters
            # This represents the rightmost position where we can start
            # a substring ending at current_index that contains all three characters
            min_index = min(last_seen_index["a"], last_seen_index["b"], last_seen_index["c"])
          
            # Add the number of valid substrings ending at current position
            # If min_index is -1, no valid substrings exist (min_index + 1 = 0)
            # Otherwise, we can start from positions 0 to min_index (inclusive)
            total_count += min_index + 1
      
        return total_count
