class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count frequency of each number in the array
        frequency_map = Counter(nums)
      
        # Special case for 1: since 1^2 = 1, we can use all 1s
        # But we need odd count for a valid subsequence (center element)
        # If count of 1s is even, we subtract 1 to make it odd
        max_length = frequency_map[1] - (frequency_map[1] % 2 ^ 1)
      
        # Remove 1 from consideration as we've already handled it
        del frequency_map[1]
      
        # Check each unique number as potential base of geometric sequence
        for base_num in frequency_map:
            current_length = 0
            current_num = base_num
          
            # Build sequence: [x, x, x^2, x^2, x^4, x^4, ...]
            # We need at least 2 occurrences to continue the pattern
            while frequency_map[current_num] > 1:
                current_num = current_num * current_num  # Square the number
                current_length += 2  # Add pair to sequence
          
            # If the final squared number exists, add it as center element
            # Otherwise, we went too far, so subtract 1 from length
            if frequency_map[current_num]:
                current_length += 1  # Add center element
            else:
                current_length -= 1  # Remove last invalid pair
          
            # Update maximum length found so far
            max_length = max(max_length, current_length)
      
        return max_length
