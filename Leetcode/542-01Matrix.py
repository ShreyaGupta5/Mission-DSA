from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        Q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    Q.append((i, j))
                else:
                    mat[i][j] = -1

        while Q:
            X, Y = Q.popleft()

            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                p, q = X + dx, Y + dy

                if 0 <= p < m and 0 <= q < n and mat[p][q] == -1:
                    mat[p][q] = mat[X][Y] + 1
                    Q.append((p, q))

        return mat
