class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Remove characters used by target[0:n-1]
        missing = 0

        for ch in target[:-1]:
            idx = ord(ch) - ord('a')
            count[idx] -= 1

            if count[idx] < 0:
                missing += 1

        # Try changing a position from right to left
        for i in range(n - 1, -1, -1):

            # If target[0:i] can be formed from s
            if missing == 0:

                current = ord(target[i]) - ord('a')

                # Find the smallest character greater than target[i]
                for j in range(current + 1, 26):

                    if count[j] > 0:
                        count[j] -= 1

                        # Prefix stays equal to target
                        ans = list(target[:i])

                        # Make this position slightly greater
                        ans.append(chr(j + ord('a')))

                        # Put remaining characters in sorted order
                        for k in range(26):
                            ans.extend([chr(k + ord('a'))] * count[k])

                        return ''.join(ans)

            # Move one position to the left.
            # target[i-1] is no longer part of the prefix.
            if i > 0:
                idx = ord(target[i - 1]) - ord('a')

                if count[idx] < 0:
                    missing -= 1

                count[idx] += 1

        return ""
