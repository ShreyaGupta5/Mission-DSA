class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: Strings must be the same length to be rotations
        # Step 2: s + s contains all possible rotations of s
        return len(s) == len(goal) and goal in (s + s)
