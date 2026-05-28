from typing import List
from math import inf


class Trie:
  
    __slots__ = ("children", "length", "idx")
  
    def __init__(self):
      
        # Array to store child nodes for each letter a-z
        self.children = [None] * 26
        # Store the minimum length of strings passing through this node
        self.length = inf
        # Store the index of the string with minimum length at this node
        self.idx = inf
  
    def insert(self, word: str, index: int) -> None:
        node = self
      
        # Update root node with minimum length word information
        if node.length > len(word):
            node.length = len(word)
            node.idx = index
      
        # Insert characters in reverse order (for suffix matching)
        for char in word[::-1]:
            # Calculate the index for this character (0-25 for a-z)
            char_index = ord(char) - ord("a")
          
            # Create new node if path doesn't exist
            if node.children[char_index] is None:
                node.children[char_index] = Trie()
          
            # Move to child node
            node = node.children[char_index]
          
            # Update this node with minimum length word information
            if node.length > len(word):
                node.length = len(word)
                node.idx = index
  
    def query(self, word: str) -> int:
        node = self
      
        # Traverse the Trie following the reverse of the query word
        for char in word[::-1]:
            char_index = ord(char) - ord("a")
          
            # Stop if no further matching suffix exists
            if node.children[char_index] is None:
                break
          
            # Move to the next node
            node = node.children[char_index]
      
        # Return the index of the best matching word at this node
        return node.idx


class Solution:
      
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        
        # Build the Trie with all container words
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)
      
        # Process each query and return results
        return [trie.query(word) for word in wordsQuery]
