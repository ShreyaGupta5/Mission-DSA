class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        from functools import lru_cache
        
        n = len(robot)
        m = len(factory)
        
        @lru_cache(None)
        def dp(i, j):
            # If all robots are assigned
            if i == n:
                return 0
            
            # If no factories left
            if j == m:
                return float('inf')
            
            # Option 1: skip this factory
            res = dp(i, j + 1)
            
            # Option 2: assign robots to this factory
            pos, cap = factory[j]
            dist = 0
            
            for k in range(1, cap + 1):
                if i + k > n:
                    break
                
                # add distance for k-th robot
                dist += abs(robot[i + k - 1] - pos)
                
                res = min(res, dist + dp(i + k, j + 1))
            
            return res
        
        return dp(0, 0)
