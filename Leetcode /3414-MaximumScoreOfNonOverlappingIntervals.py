import functools
import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        # 1. Store intervals with their original index: (start, end, weight, original_index)
        # We sort them by start time to process them sequentially.
        A = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(A)
        
        # Extract only start times to use for fast binary search looking for next non-overlapping interval
        starts = [x[0] for x in A]
        
        @functools.lru_cache(None)
        def dp(i: int, count: int) -> tuple[int, tuple[int, ...]]:
            """
            Returns a tuple: (max_score, sorted_tuple_of_original_indices)
            For intervals from index i to n-1, choosing at most `count` intervals.
            """
            if i == n or count == 0:
                return (0, ())
            
            # Option 1: Skip the current interval
            res_score, res_indices = dp(i + 1, count)
            
            # Option 2: Take the current interval
            start, end, weight, orig_idx = A[i]
            
            # Find the next interval that starts strictly after the current interval ends.
            # Two intervals overlap if they share any points (even boundaries).
            # So next interval must have start > current_end
            next_idx = bisect.bisect_right(starts, end)
            
            next_score, next_indices = dp(next_idx, count - 1)
            take_score = weight + next_score
            
            # Combine the current original index with the future chosen indices, then sort them ascendingly
            take_indices = tuple(sorted(next_indices + (orig_idx,)))
            
            # Evaluate the best choice
            if take_score > res_score:
                res_score = take_score
                res_indices = take_indices
            elif take_score == res_score:
                # Tie-breaking rule: Pick the lexicographically smaller indices tuple
                if take_indices < res_indices:
                    res_indices = take_indices
                    
            return (res_score, res_indices)
        
        # We can pick up to 4 intervals starting from index 0
        score, ans_tuple = dp(0, 4)
        return list(ans_tuple)
