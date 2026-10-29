class SegmentTree:
    def __init__(self, n, initial_values):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(initial_values, 1, 0, n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2 * node, start, mid)
        self.build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 ^ p2


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Step 1: Build the Adjacency List
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: HLD Variables
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        size = [0] * n
        cur_pos = 0

        # Step 3: First DFS to find heavy edges, sizes, depths, and parents
        # Using iterative DFS to avoid recursion depth issues in Python
        stack = [(0, -1, 0)]  # (node, parent_node, state)
        # States: 0 = pre-visit, 1 = post-visit child loop processing
        # We can also use a standard stack approach for post-order
        order = []
        st = [0]
        visited = [False] * n
        visited[0] = True
        parent[0] = -1
        depth[0] = 0
        
        # Iterative post-order layout gathering
        queue = [0]
        head_q = 0
        while head_q < len(queue):
            u = queue[head_q]
            head_q += 1
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    queue.append(v)
        
        # Calculate sizes and heavy edges backwards
        size = [1] * n
        for u in reversed(order):
            if u == 0: continue
            p = parent[u]
            size[p] += size[u]
            if heavy[p] == -1 or size[u] > size[heavy[p]]:
                heavy[p] = u

        # Step 4: Second DFS to decompose paths into heavy chains
        cur_pos = 0
        head[0] = 0
        # Re-use order array or stack for decomposition
        # We can use a standard stack prioritizing the heavy child
        stack = [0]
        while stack:
            u = stack.pop()
            pos[u] = cur_pos
            cur_pos += 1
            
            # Put light children first so heavy child is popped last (processed first)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    head[v] = v
                    stack.append(v)
            if heavy[u] != -1:
                head[heavy[u]] = head[u]
                stack.append(heavy[u])

        # Step 5: Initialize values for the segment tree based on position mappings
        flat_arr = [0] * n
        for i in range(n):
            flat_arr[pos[i]] = 1 << (ord(s[i]) - ord('a'))

        seg_tree = SegmentTree(n, flat_arr)

        # Step 6: Define Path Query Helper
        def query_path(u, v):
            res_mask = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res_mask ^= seg_tree.query(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res_mask ^= seg_tree.query(1, 0, n - 1, pos[u], pos[v])
            return res_mask

        # Step 7: Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                val = 1 << (ord(c) - ord('a'))
                seg_tree.update(1, 0, n - 1, pos[u], val)
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                # Check if at most one bit is set
                is_palindrome = (mask == 0) or ((mask & (mask - 1)) == 0)
                ans.append(is_palindrome)

        return ans
