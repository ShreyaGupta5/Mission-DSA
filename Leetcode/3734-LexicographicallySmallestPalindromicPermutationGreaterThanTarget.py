from collections import Counter
import string

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # 1. Check if a valid palindrome permutation can even be formed
        odd_chars = [ch for ch in cnt if cnt[ch] % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid = odd_chars[0] if odd_chars else ""
        
        # 2. Extract the available characters for the left half
        half_chars = []
        for ch in sorted(cnt.keys()):
            half_chars.extend([ch] * (cnt[ch] // 2))
        
        half_len = n // 2
        target_half = target[:half_len]
        
        # 3. Greedy Placement Logic
        def get_smallest_permutation(available_counts, prefix, exact_match):
            res = list(prefix)
            if exact_match:
                for i in range(len(res), half_len):
                    t_ch = target_half[i]
                    if available_counts[t_ch] > 0:
                        available_counts[t_ch] -= 1
                        res.append(t_ch)
                    else:
                        return None
                return "".join(res)
            else:
                for ch in string.ascii_lowercase:
                    while available_counts[ch] > 0:
                        res.append(ch)
                        available_counts[ch] -= 1
                return "".join(res)

        best_left = None
        
        # Try every possible prefix length matching target_half
        for match_len in range(half_len, -1, -1):
            counts = Counter(half_chars)
            possible = True
            prefix = []
            
            # Form the exact matching prefix segment
            for i in range(match_len):
                t_ch = target_half[i]
                if counts[t_ch] > 0:
                    counts[t_ch] -= 1
                    prefix.append(t_ch)
                else:
                    possible = False
                    break
            
            if not possible:
                continue
                
            if match_len == half_len:
                # Case A: Left half matches target_half exactly
                left = get_smallest_permutation(counts.copy(), prefix, True)
                if left is not None:
                    full = left + mid + left[::-1]
                    if full > target:
                        best_left = left
                        break
            else:
                # Case B: Match up to match_len, then pick a STRICTLY GREATER character next
                next_target_ch = target_half[match_len]
                found_greater = False
                
                for code in range(ord(next_target_ch) + 1, ord('z') + 1):
                    next_ch = chr(code)
                    if counts[next_ch] > 0:
                        counts[next_ch] -= 1
                        prefix.append(next_ch)
                        found_greater = True
                        break
                
                if found_greater:
                    left = get_smallest_permutation(counts, prefix, False)
                    if left is not None:
                        best_left = left
                        break
        
        if best_left is None:
            return ""
            
        return best_left + mid + best_left[::-1]
