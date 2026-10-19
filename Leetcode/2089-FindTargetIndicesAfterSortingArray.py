class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sort the array in ascending order (modifies in-place)
        nums.sort()

        # Use list comprehension to collect all indices where value equals target
        # enumerate() provides (index, value) pairs for each element
        result = [i for i, v in enumerate(nums) if v == target]

        return result
