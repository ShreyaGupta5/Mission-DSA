class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array in ascending order
        arr.sort()
      
        # First element must be 1 according to problem constraints
        arr[0] = 1
      
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # Calculate the difference needed to maintain the constraint
            # that adjacent elements differ by at most 1
            difference = max(0, arr[i] - arr[i - 1] - 1)
          
            # Decrease current element to satisfy the constraint
            arr[i] -= difference
      
        # Return the maximum element in the modified array
        return max(arr)
