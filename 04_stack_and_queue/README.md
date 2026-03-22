# 04 - Stack and Queue

Stacks handle "most recent unmatched" problems. Queues handle "process in order" and BFS. Both are fundamental building blocks.

## Core Patterns

### Stack
1. **Matching / undo**: Parentheses, brackets, nested structures
2. **Monotonic stack**: Next greater/smaller element
3. **Expression evaluation**: Infix/postfix parsing
4. **DFS simulation**: Iterative DFS using explicit stack

### Queue
1. **BFS / level-order**: Process nodes level by level
2. **Shortest path (unweighted)**: BFS gives shortest steps
3. **Sliding window max**: Monotonic deque

## Recognition Clues

**Use a stack when:**
- "Most recent unmatched item"
- "Next greater/smaller element"
- Recursive process needs iterative simulation
- Nested structure validation

**Use a queue when:**
- Process nodes level by level
- Shortest number of steps in unweighted graph/grid
- FIFO ordering matters

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | ⬜ | Stack matching |
| 2 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | ⬜ | Auxiliary stack |
| 3 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | ⬜ | Stack evaluation |
| 4 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | ⬜ | Stack + backtracking |
| 5 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | ⬜ | Monotonic stack |
| 6 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | ⬜ | Stack simulation |
| 7 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | ⬜ | Monotonic stack |

## Common Mistakes
- Using a list as queue (`list.pop(0)` is O(n) — use `deque.popleft()`)
- Forgetting to check `if stack` before `stack.pop()`
- Monotonic stack: confusing "increasing" vs "decreasing" direction
