class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        visited = set()

        def dfs(i):
            # Out of bounds or already visited
            if i < 0 or i >= n or i in visited:
                return False

            # Reached value 0
            if arr[i] == 0:
                return True

            visited.add(i)

            # Jump left or right
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
