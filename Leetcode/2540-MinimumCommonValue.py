class Solution:
    def getCommon(self, nums1, nums2):
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):

            # Common value found
            if nums1[i] == nums2[j]:
                return nums1[i]

            # Move smaller value pointer
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
