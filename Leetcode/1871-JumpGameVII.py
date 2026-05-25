class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # If the last character is '1', we can never reach it
        if s[n - 1] == '1':
            return False
            
        dp = [True] + [False] * (n - 1)
        reachable_count = 0
        
        for i in range(1, n):
            # Maintain the sliding window of size [i - maxJump, i - minJump]
            if i >= minJump:
                reachable_count += dp[i - minJump]
            if i > maxJump:
                reachable_count -= dp[i - maxJump - 1]
                
            # A spot is reachable if it's a '0' and we have at least one reachable jump in our window
            if reachable_count > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[n - 1]
