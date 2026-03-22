# 07 - Trees

A major stage. Tree problems train recursive decomposition. **Practice every traversal both iteratively and recursively.**

## Core Patterns

### Traversals (MUST master both iterative and recursive)

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Preorder** | Root → Left → Right | Copy tree, serialize |
| **Inorder** | Left → Root → Right | BST sorted order |
| **Postorder** | Left → Right → Root | Delete tree, subtree computation |
| **Level-order** | Level by level (BFS) | Level-based problems |

### Recursive Templates

```python
# Preorder
def preorder(node):
    if not node: return
    process(node)          # Root first
    preorder(node.left)
    preorder(node.right)

# Inorder
def inorder(node):
    if not node: return
    inorder(node.left)
    process(node)          # Root in middle
    inorder(node.right)

# Postorder
def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    process(node)          # Root last
```

### Iterative Templates

```python
# Preorder (iterative)
def preorder(root):
    if not root: return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)  # Right first (LIFO)
        if node.left: stack.append(node.left)
    return result

# Inorder (iterative)
def inorder(root):
    stack, result, curr = [], [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

# Postorder (iterative - reverse of modified preorder)
def postorder(root):
    if not root: return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left: stack.append(node.left)   # Left first this time
        if node.right: stack.append(node.right)
    return result[::-1]  # Reverse

# Level-order (BFS)
from collections import deque
def levelorder(root):
    if not root: return []
    queue, result = deque([root]), []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### Problem-Solving Patterns

1. **Subtree return**: Each recursive call returns info about its subtree
2. **Path-based**: Track path from root or between nodes
3. **Level-based**: BFS with level tracking
4. **Top-down vs bottom-up**: Pass info down (params) vs return info up (return values)

## Recognition Clues

- "What information should each subtree return?" → postorder / bottom-up
- "Process level by level" → BFS
- "Path from root to leaf" → preorder / top-down
- "Sorted order from BST" → inorder

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | ⬜ | Recursive swap |
| 2 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | ⬜ | DFS bottom-up / BFS |
| 3 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | ⬜ | Postorder + global max |
| 4 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | ⬜ | Bottom-up height check |
| 5 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | ⬜ | Simultaneous DFS |
| 6 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | ⬜ | DFS + Same Tree |
| 7 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | ⬜ | BST value-based split |
| 8 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | ⬜ | BFS with level grouping |
| 9 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | ⬜ | BFS last-of-level / DFS |
| 10 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | ⬜ | Preorder + track max |
| 11 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | ⬜ | Inorder or range DFS |
| 12 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | ⬜ | Inorder traversal |
| 13 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | ⬜ | Recursive build |
| 14 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | ⬜ | Postorder + global max |
| 15 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | ⬜ | Preorder + queue rebuild |

## Important: Iterative vs Recursive

For EVERY tree problem, ask yourself:
1. Can I solve this recursively? (usually yes)
2. Can I solve this iteratively? (usually with stack/queue)
3. Which traversal order does this problem need?

Practice both. Interviews may ask you to convert one to the other.

## Common Mistakes
- Forgetting base case `if not node: return`
- Confusing preorder/postorder — think about WHEN you process the root
- BFS: forgetting `for _ in range(len(queue))` to process one level at a time
- Returning wrong value from recursive call (returning None when you meant to propagate)
