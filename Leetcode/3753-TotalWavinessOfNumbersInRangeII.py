from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def count_waviness_up_to(n: int) -> int:
            if n < 100:
                return 0
            
            s = str(n)
            length = len(s)
            
            @lru_cache(None)
            def dp(idx: int, prev_digit: int, prev_prev_digit: int, is_started: bool, is_limit: bool) -> int:
                # Base case: if we reach the end, we return 0 because no more peaks/valleys can be formed
                if idx == length:
                    return 0
                
                # Determine the upper bound for the current digit position
                high = int(s[idx]) if is_limit else 9
                total_waviness = 0
                
                for d in range(high + 1):
                    next_limit = is_limit and (d == high)
                    
                    if not is_started:
                        if d == 0:
                            # Still processing leading zeros
                            total_waviness += dp(idx + 1, -1, -1, False, next_limit)
                        else:
                            # Placed the very first valid digit
                            total_waviness += dp(idx + 1, d, -1, True, next_limit)
                    else:
                        # Valid digits are active
                        current_wave = 0
                        # Check if prev_digit forms a peak or valley
                        if prev_prev_digit != -1:
                            if prev_digit > prev_prev_digit and prev_digit > d:
                                current_wave = 1  # Peak detected
                            elif prev_digit < prev_prev_digit and prev_digit < d:
                                current_wave = 1  # Valley detected
                        
                        # In addition to the local match, add the cumulative downstream results.
                        # However, we only count the 'current_wave' structure if this path completes safely,
                        # which means multiplying it by the total combinations of remaining valid suffix branches.
                        # To simplify, we count how many times this specific structural property triggers:
                        total_waviness += current_wave * count_combinations(idx + 1, next_limit) + \
                                          dp(idx + 1, d, prev_digit, True, next_limit)
                                          
                return total_waviness

            @lru_cache(None)
            def count_combinations(idx: int, is_limit: bool) -> int:
                # Helper to count how many valid standard numbers can be formed from 'idx' to the end
                if idx == length:
                    return 1
                high = int(s[idx]) if is_limit else 9
                res = 0
                for d in range(high + 1):
                    res += count_combinations(idx + 1, is_limit and (d == high))
                return res

            return dp(0, -1, -1, False, True)

        return count_waviness_up_to(num2) - count_waviness_up_to(num1 - 1)
