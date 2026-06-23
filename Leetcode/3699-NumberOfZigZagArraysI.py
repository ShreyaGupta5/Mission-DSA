class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Length 2 initialization
        up = [i for i in range(m)]              # values smaller than i
        down = [m - 1 - i for i in range(m)]   # values greater than i

        if n == 2:
            return sum(up) + sum(down)

        for _ in range(3, n + 1):
            # Prefix sums of down
            pref_down = [0] * (m + 1)
            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD

            # Prefix sums of up
            pref_up = [0] * (m + 1)
            for i in range(m):
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for i in range(m):
                # sum(down[0:i])
                new_up[i] = pref_down[i]

                # sum(up[i+1:m])
                new_down[i] = (total_up - pref_up[i + 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD
