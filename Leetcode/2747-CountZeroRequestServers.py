from collections import Counter

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # 1. Sort the logs based on timestamp
        logs.sort(key=lambda log: log[1])
        
        # 2. Pair each query with its original index and sort them chronologically
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        # 3. Initialize variables
        ans = [0] * len(queries)
        active_servers = Counter()
        
        # Two pointers tracking the valid log window bounds [left, right)
        left = 0
        right = 0
        num_logs = len(logs)
        
        # 4. Process each query using the sliding window
        for original_idx, query_time in sorted_queries:
            window_start = query_time - x
            window_end = query_time
            
            # Expand the right side of the window: include all logs up to window_end
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                active_servers[server_id] += 1
                right += 1
                
            # Shrink the left side of the window: exclude all logs before window_start
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1
                
            # The number of zero-request servers is total servers minus active servers
            ans[original_idx] = n - len(active_servers)
            
        return ans
