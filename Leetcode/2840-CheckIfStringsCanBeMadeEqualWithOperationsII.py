class Solution:
    def checkStrings(self, s: str, t: str) -> bool:
        # Separate even and odd indexed characters
        s_even = sorted(s[i] for i in range(0, len(s), 2))
        s_odd = sorted(s[i] for i in range(1, len(s), 2))
        
        t_even = sorted(t[i] for i in range(0, len(t), 2))
        t_odd = sorted(t[i] for i in range(1, len(t), 2))
        
        # Compare both parts
        return s_even == t_even and s_odd == t_odd
