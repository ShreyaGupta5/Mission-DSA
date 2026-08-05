from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    q.append(nxt)

        # If any non-suspicious method calls a suspicious method,
        # we cannot remove them.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
