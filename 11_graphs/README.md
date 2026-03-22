# 11 - Graphs

Many grid problems are really graph problems. BFS/DFS patterns become much more general here. **Practice both iterative and recursive for DFS.**

## Core Patterns

### DFS (Recursive + Iterative)

```python
# Recursive DFS
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# Iterative DFS
def dfs_iterative(start):
    stack, visited = [start], set()
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### BFS (Iterative + can be recursive via level processing)

```python
# Standard BFS
from collections import deque
def bfs(start):
    queue, visited = deque([start]), {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Other Patterns
1. **Connected components**: DFS/BFS from each unvisited node
2. **Cycle detection**: DFS with "in current path" tracking
3. **Topological sort**: Kahn's (BFS) or DFS with finish order
4. **Union Find**: Disjoint set for dynamic connectivity
5. **Grid as graph**: 4-directional neighbors, bounds checking

## Recognition Clues

- States are connected, can move between nodes/cells
- "Number of islands" / connected regions
- Shortest path in unweighted setting → BFS
- Prerequisite/dependency order → topological sort
- Dynamic connectivity → Union Find

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | ⬜ | Grid DFS/BFS |
| 2 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | ⬜ | DFS area count |
| 3 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | ⬜ | BFS/DFS + hash map |
| 4 | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | Medium | ⬜ | Multi-source BFS |
| 5 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | ⬜ | Multi-source BFS |
| 6 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | ⬜ | Reverse DFS from edges |
| 7 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | ⬜ | Border DFS |
| 8 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | ⬜ | Cycle detection / topo sort |
| 9 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | ⬜ | Topological sort |
| 10 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium | ⬜ | Connected + no cycle |
| 11 | [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium | ⬜ | Union Find / DFS |
| 12 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | ⬜ | Union Find |
| 13 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | ⬜ | BFS shortest path |

## Important: Iterative vs Recursive

- **DFS**: Practice BOTH iterative (stack) and recursive
- **BFS**: Iterative with queue is standard; understand why recursive BFS is rarely used (level-order needs a queue)
- **Topological Sort**: Know BOTH Kahn's algorithm (BFS) and DFS-based approach

## Common Mistakes
- Grid DFS: forgetting to mark visited BEFORE adding to stack/queue (causes duplicates)
- Cycle detection: confusing "visited globally" vs "in current DFS path"
- Topological sort: forgetting to check for cycles (if cycle exists, no valid ordering)
