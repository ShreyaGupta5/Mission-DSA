class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats for each row
        for r, s in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(s)

        # Initially, every row can fit 2 families
        ans = 2 * n

        for seats in rows.values():

            # Left group: 2,3,4,5
            left = not any(s in seats for s in [2, 3, 4, 5])

            # Middle group: 4,5,6,7
            middle = not any(s in seats for s in [4, 5, 6, 7])

            # Right group: 6,7,8,9
            right = not any(s in seats for s in [6, 7, 8, 9])

            if left and right:
                # Two families can sit
                continue

            elif left or middle or right:
                # Only one family can sit
                ans -= 1

            else:
                # No family can sit
                ans -= 2

        return ans
