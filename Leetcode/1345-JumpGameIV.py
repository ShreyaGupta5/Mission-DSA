import collections
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Group indices by value for O(1) access to same-value indices
        graph = collections.defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        # BFS setup
        queue = collections.deque([0])
        seen = {0}
        step = 0
        
        while queue:
            # Process all nodes at current level
            for _ in range(len(queue)):
                i = queue.popleft()
                
                # Reached last index
                if i == n - 1:
                    return step
                
                val = arr[i]
                
                # Jump to all indices with same value
                for j in graph[val]:
                    if j not in seen:
                        seen.add(j)
                        queue.append(j)
                
                # Clear to avoid reprocessing same-value jumps
                graph[val] = []
                
                # Jump to i + 1
                if i + 1 < n and i + 1 not in seen:
                    seen.add(i + 1)
                    queue.append(i + 1)
                
                # Jump to i - 1
                if i - 1 >= 0 and i - 1 not in seen:
                    seen.add(i - 1)
                    queue.append(i - 1)
            
            step += 1
        
        return -1
