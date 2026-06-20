class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])

        if not any(r[0] == n for r in restrictions):
            restrictions.append([n, n - 1])

        restrictions.sort()

        # Left to Right
        for i in range(1, len(restrictions)):
            pos1, h1 = restrictions[i - 1]
            pos2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (pos2 - pos1))

        # Right to Left
        for i in range(len(restrictions) - 2, -1, -1):
            pos1, h1 = restrictions[i]
            pos2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (pos2 - pos1))

        ans = 0

        # Find maximum peak between consecutive restrictions
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            dist = x2 - x1
            peak = (h1 + h2 + dist) // 2
            ans = max(ans, peak)

        return ans
