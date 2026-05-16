class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is in left half including mid
            elif nums[mid] < nums[right]:
                right = mid

            # Duplicate case
            else:
                right -= 1

        return nums[left]
