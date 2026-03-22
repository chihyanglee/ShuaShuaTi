# 00 - Python Toolkit for DSA

Master these Python tools before diving into problems. Weak Python fluency causes more LeetCode struggles than weak algorithm knowledge.

## Core Tools to Master

### Data Structures
| Tool | Use Case | Example |
|------|----------|---------|
| `list` | Dynamic array, stack | `arr.append()`, `arr.pop()` |
| `dict` | Hash map, frequency count | `d[key] = d.get(key, 0) + 1` |
| `set` | O(1) membership, dedup | `if x in seen` |
| `collections.Counter` | Frequency counting | `Counter("aabbc")` → `{'a':2, 'b':2, 'c':1}` |
| `collections.defaultdict` | Auto-init dict | `defaultdict(list)` |
| `collections.deque` | Queue, BFS | `deque.append()`, `deque.popleft()` |
| `heapq` | Min heap, top-k | `heappush()`, `heappop()` |

### Key Operations
| Operation | Pattern | Time |
|-----------|---------|------|
| List slicing | `arr[i:j]`, `arr[::-1]` | O(k) |
| Sorting with key | `sorted(arr, key=lambda x: x[1])` | O(n log n) |
| Enumerate | `for i, val in enumerate(arr)` | O(n) |
| Zip | `for a, b in zip(list1, list2)` | O(n) |
| List comprehension | `[x*2 for x in arr if x > 0]` | O(n) |
| String join | `"".join(chars)` | O(n) |
| `divmod` | `q, r = divmod(n, d)` | O(1) |
| `bisect` | Binary search in sorted list | O(log n) |

### Common Patterns

```python
# Frequency count
from collections import Counter
freq = Counter(arr)

# Default dict for grouping
from collections import defaultdict
groups = defaultdict(list)
for item in arr:
    groups[key(item)].append(item)

# BFS template
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# Heap - top k smallest
import heapq
heapq.nsmallest(k, arr)
# top k largest (use negative for max heap)
heap = [-x for x in arr]
heapq.heapify(heap)
```

## Practice Goals
- [ ] Write clean loops without off-by-one errors
- [ ] Count frequencies fluently with `Counter` and `dict`
- [ ] Use `set` for O(1) lookups without thinking
- [ ] Use `deque` for BFS naturally
- [ ] Use `heapq` for priority problems
- [ ] Sort with custom keys confidently
- [ ] Manipulate strings without confusion (immutable!)
