from typing import List


class Solution:

  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)

    # 1. Build the initial adjacency list
    tree = [[] for _ in range(n)]
    for i in range(1, n):
      tree[parent[i]].append(i)

    # 2. First DFS: Find the closest ancestor with the same character
    new_parent = list(parent)
    last_seen = [-1] * 26  # Tracks the deepest ancestor node for 'a'-'z'

    def find_new_parents(u: int):
      char_idx = ord(s[u]) - ord('a')
      prev_ancestor = last_seen[char_idx]

      # If a valid ancestor with the same character exists, update parent
      if prev_ancestor != -1:
        new_parent[u] = prev_ancestor

      # Mark current node as the most recent ancestor for this character
      last_seen[char_idx] = u

      for v in tree[u]:
        find_new_parents(v)

      # Backtrack: restore the previous ancestor state for sibling branches
      last_seen[char_idx] = prev_ancestor

    find_new_parents(0)

    # 3. Build the updated tree using new_parent
    updated_tree = [[] for _ in range(n)]
    for i in range(1, n):
      updated_tree[new_parent[i]].append(i)

    # 4. Second DFS: Calculate subtree sizes on the modified tree
    ans = [1] * n

    def count_sizes(u: int) -> int:
      for v in updated_tree[u]:
        ans[u] += count_sizes(v)
      return ans[u]

    count_sizes(0)
    return ans
