class Solution:
  def minInsertions(self, s: str) -> int:
    res = 0
    left = 0
    i = 0
    n = len(s)

    while i < n:
      if s[i] == '(':
        left += 1
        i += 1
      else:
        # Check if the next character is also a ')'
        if i + 1 < n and s[i + 1] == ')':
          i += 2
        else:
          # Missing one ')' to form a pair '))'
          res += 1
          i += 1

        # Match the '))' pair with an open '('
        if left > 0:
          left -= 1
        else:
          # No open '(' available, need to insert one '('
          res += 1

    # Any remaining open '(' need two ')' each
    return res + left * 2
