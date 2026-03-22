# 08 - Tries

Prefix tree — specialized tree for string problems. Efficient for prefix matching and word search.

## Core Patterns

1. **Insert / search / startsWith**: Basic trie operations
2. **Word search in grid**: Trie + DFS/backtracking
3. **Autocomplete / prefix matching**: Walk trie by prefix

## Trie Template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

## Recognition Clues

- "Prefix matching" or "starts with"
- "Word dictionary" with repeated lookups
- "Word search in grid" with a word list
- Multiple string comparisons that share prefixes

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | ⬜ | Basic trie |
| 2 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | ⬜ | Trie + DFS for '.' |
| 3 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | ⬜ | Trie + grid backtracking |

## Common Mistakes
- Using an array of 26 vs dict for children (dict is more Pythonic and flexible)
- Forgetting to mark `is_end` during insert
- Word Search II: not pruning visited nodes during backtracking
