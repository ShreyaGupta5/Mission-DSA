class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree nodes store: sum of values, sum of squared values, lazy tag
        tree_sum = [0] * (4 * n)
        tree_sq_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, start, end):
            if lazy[node] != 0:
                val = lazy[node]
                mid = (start + end) // 2
                
                # Update left child
                left = 2 * node
                length_left = mid - start + 1
                tree_sq_sum[left] = (tree_sq_sum[left] + 2 * val * tree_sum[left] + val * val * length_left) % MOD
                tree_sum[left] = (tree_sum[left] + val * length_left) % MOD
                lazy[left] = (lazy[left] + val) % MOD
                
                # Update right child
                right = 2 * node + 1
                length_right = end - mid
                tree_sq_sum[right] = (tree_sq_sum[right] + 2 * val * tree_sum[right] + val * val * length_right) % MOD
                tree_sum[right] = (tree_sum[right] + val * length_right) % MOD
                lazy[right] = (lazy[right] + val) % MOD
                
                lazy[node] = 0

        def update(node, start, end, l, r, val):
            if r < start or end < l:
                return
            if l <= start and end <= r:
                length = end - start + 1
                tree_sq_sum[node] = (tree_sq_sum[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
                tree_sum[node] = (tree_sum[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq_sum[node] = (tree_sq_sum[2 * node] + tree_sq_sum[2 * node + 1]) % MOD

        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree_sq_sum[node]
            push(node, start, end)
            mid = (start + end) // 2
            return (query(2 * node, start, mid, l, r) + query(2 * node + 1, mid + 1, end, l, r)) % MOD

        last_seen = {}
        ans = 0
        current_sum_sq = 0
        
        for r_idx, x in enumerate(nums):
            l_idx = last_seen.get(x, -1) + 1
            last_seen[x] = r_idx
            
            # Update range [l_idx, r_idx] by adding 1
            update(1, 0, n - 1, l_idx, r_idx, 1)
            
            # Query sum of squares from index 0 to r_idx
            current_sum_sq = query(1, 0, n - 1, 0, r_idx)
            ans = (ans + current_sum_sq) % MOD
            
        return ans
