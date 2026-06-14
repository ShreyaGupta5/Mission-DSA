class Solution:
    def pairSum(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        ans = 0
        n = len(nums)

        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])

        return ans
