import collections

class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        # Union-Find: Find with Path Compression
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        # Union-Find: Union by connecting components
        for u, v in allowedSwaps:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parent[root_u] = root_v

        # Group elements of 'source' by their connected component root
        groups = collections.defaultdict(collections.Counter)
        for i in range(n):
            root = find(i)
            groups[root][source[i]] += 1

        # Calculate Hamming Distance
        hamming_distance = 0
        for i in range(n):
            root = find(i)
            val = target[i]
            # If the target value exists in this connected group, "use" it
            if groups[root][val] > 0:
                groups[root][val] -= 1
            else:
                # If target value is not available in the group, it's a mismatch
                hamming_distance += 1
                
        return hamming_distance
