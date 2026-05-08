from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # Store indices divisible by each number
        div_map = defaultdict(list)

        for i, x in enumerate(nums):
            d = 2
            temp = x

            while d * d <= temp:
                if temp % d == 0:
                    div_map[d].append(i)

                    while temp % d == 0:
                        temp //= d
                d += 1

            if temp > 1:
                div_map[temp].append(i)

        # Check prime
        def is_prime(x):
            if x < 2:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True

        q = deque([(0, 0)])  # (index, steps)
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # Adjacent moves
            for ni in [i - 1, i + 1]:
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append((ni, steps + 1))

            # Prime teleport
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                used_prime.add(val)

                for ni in div_map[val]:
                    if not visited[ni]:
                        visited[ni] = True
                        q.append((ni, steps + 1))

        return -1
