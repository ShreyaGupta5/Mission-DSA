import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        def can_finish(t):
            total = 0
            
            for w in workerTimes:
                x = int(math.sqrt(2*t/w + 0.25) - 0.5)
                total += x
                
                if total >= mountainHeight:
                    return True
            
            return False
        
        left, right = 1, 10**16
        
        while left < right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
