class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s = []
            # Step through the string in chunks of size k
            for i in range(0, len(s), k):
                chunk = s[i : i + k]
                # Sum the integer value of each digit in the chunk
                chunk_sum = sum(int(digit) for digit in chunk)
                next_s.append(str(chunk_sum))
            # Join the summed chunks to form the new string
            s = "".join(next_s)
        return s
