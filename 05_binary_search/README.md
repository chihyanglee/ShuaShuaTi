# 05 - Binary Search

Not just for sorted arrays — binary search on answer space is a powerful technique for optimization problems.

## Core Patterns

1. **Classic binary search**: Find target in sorted array
2. **Lower bound / upper bound**: Find insertion point or boundary
3. **Rotated array search**: Modified binary search with pivot
4. **Binary search on answer**: "What's the minimum/maximum X such that condition holds?"

## Recognition Clues

- Search space is ordered
- Answer has a monotonic property (if X works, all larger/smaller also work)
- "Find minimum value that satisfies..."
- Sorted or rotated sorted input
- O(log n) requirement hints at binary search

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | ⬜ | Classic |
| 2 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | ⬜ | Flatten + binary search |
| 3 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | ⬜ | BS on answer |
| 4 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | ⬜ | Rotated pivot |
| 5 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | ⬜ | Rotated + target |
| 6 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | ⬜ | BS on timestamps |
| 7 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | ⬜ | BS on partition |

## Common Mistakes
- Off-by-one: `left <= right` vs `left < right` (depends on template)
- Wrong mid calculation: use `left + (right - left) // 2` to avoid overflow
- BS on answer: getting the condition/predicate function wrong
