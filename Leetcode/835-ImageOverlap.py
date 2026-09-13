class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        count = {}

        for r1 in range(n):
            for c1 in range(n):
                if img1[r1][c1] == 1:

                    for r2 in range(n):
                        for c2 in range(n):
                            if img2[r2][c2] == 1:

                                dr = r1 - r2
                                dc = c1 - c2

                                key = (dr, dc)

                                count[key] = count.get(key, 0) + 1

        return max(count.values(), default=0)
