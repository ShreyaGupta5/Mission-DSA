class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Initialize three lists to store elements based on their relation to pivot
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []
      
        # Iterate through each element and categorize based on pivot comparison
        for num in nums:
            if num < pivot:
                # Element is less than pivot
                less_than_pivot.append(num)
            elif num == pivot:
                # Element equals pivot
                equal_to_pivot.append(num)
            else:
                # Element is greater than pivot
                greater_than_pivot.append(num)
      
        # Concatenate the three lists in order and return
        return less_than_pivot + equal_to_pivot + greater_than_pivot
