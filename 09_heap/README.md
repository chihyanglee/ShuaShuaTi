# 09 - Heap / Priority Queue

Heaps appear in top-k, scheduling, merge-k, and stream problems. Python's `heapq` is a min-heap.

## Core Patterns

1. **Min heap**: Default `heapq` — repeatedly get smallest
2. **Max heap**: Negate values (`-val`) to simulate max heap
3. **Size-k heap**: Maintain heap of size k for top-k problems
4. **Two heaps**: Max heap + min heap for median problems
5. **Merge k sorted**: Heap of (value, index) from each source

## Recognition Clues

- "Kth largest/smallest"
- "Top k frequent/closest"
- Repeatedly need the smallest/largest item
- Processing data streams
- Merging multiple sorted sources
- Scheduling with priorities

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | ⬜ | Min heap of size k |
| 2 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | ⬜ | Max heap simulation |
| 3 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | ⬜ | Min heap by distance |
| 4 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | ⬜ | Quickselect or heap |
| 5 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | ⬜ | Max heap + cooldown |
| 6 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | ⬜ | Merge k feeds |
| 7 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | ⬜ | Two heaps |

## Common Mistakes
- Forgetting Python's `heapq` is min-heap only — negate for max
- `heapq.nlargest(k, arr)` is O(n + k log n), not always best for repeated queries
- Not using tuples correctly for tie-breaking: `(priority, counter, item)`
