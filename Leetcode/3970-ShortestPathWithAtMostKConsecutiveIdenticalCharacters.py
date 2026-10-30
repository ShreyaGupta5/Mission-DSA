import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Min-heap stores: (total_weight, current_node, consecutive_count)
        # Start at node 0 with weight 0 and 1 consecutive character (labels[0])
        pq = [(0, 0, 1)]
        
        # Best distance map: dist[(node, count)] = min_weight
        dist = {}
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return w
                
            if dist.get((u, count), float('inf')) < w:
                continue
            dist[(u, count)] = w
            
            for v, weight in adj[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                    if new_count <= k:
                        next_w = w + weight
                        if next_w < dist.get((v, new_count), float('inf')):
                            dist[(v, new_count)] = next_w
                            heapq.heappush(pq, (next_w, v, new_count))
                else:
                    new_count = 1
                    next_w = w + weight
                    if next_w < dist.get((v, new_count), float('inf')):
                        dist[(v, new_count)] = next_w
                        heapq.heappush(pq, (next_w, v, new_count))
                        
        return -1
