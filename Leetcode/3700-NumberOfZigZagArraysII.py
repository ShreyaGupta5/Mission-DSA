class Solution:
    MOD = 10**9 + 7

    def mat_mul(self, A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]

        for i in range(n):
            for k in range(n):
                if A[i][k] == 0:
                    continue
                aik = A[i][k]
                for j in range(n):
                    if B[k][j]:
                        C[i][j] = (C[i][j] + aik * B[k][j]) % self.MOD

        return C

    def mat_pow(self, base, exp):
        n = len(base)

        res = [[0] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 1

        while exp:
            if exp & 1:
                res = self.mat_mul(base, res)

            base = self.mat_mul(base, base)
            exp >>= 1

        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        S = 2 * m

        # states:
        # 0..m-1      = down
        # m..2m-1     = up
        T = [[0] * S for _ in range(S)]

        # down[x] -> up[y] if y < x
        for x in range(m):
            for y in range(x):
                T[m + y][x] = 1

        # up[x] -> down[y] if y > x
        for x in range(m):
            for y in range(x + 1, m):
                T[y][m + x] = 1

        P = self.mat_pow(T, n - 1)

        init = [1] * S

        ans = 0
        for i in range(S):
            cur = 0
            for j in range(S):
                cur = (cur + P[i][j] * init[j]) % self.MOD
            ans = (ans + cur) % self.MOD

        return ans
