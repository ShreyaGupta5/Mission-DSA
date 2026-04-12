from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        @lru_cache(None)
        def get_dist(c1, c2):
            if c1 == 26 or c2 == 26: return 0
            x1, y1 = divmod(c1, 6)
            x2, y2 = divmod(c2, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        @lru_cache(None)
        def dp(idx, f1, f2):
            if idx == len(word):
                return 0
            
            char_code = ord(word[idx]) - ord('A')
            
            # Move finger 1
            cost1 = get_dist(f1, char_code) + dp(idx + 1, char_code, f2)
            # Move finger 2
            cost2 = get_dist(f2, char_code) + dp(idx + 1, f1, char_code)
            
            return min(cost1, cost2)
        
        # Initial positions are free, so we use a dummy 26
        return dp(0, 26, 26)
