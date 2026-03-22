# 02 - Two Pointers

One of the most common interview patterns. Learn to shrink search space by moving pointers based on invariants.

## Core Patterns

1. **Opposite-direction pointers**: Start from both ends, move inward
2. **Same-direction pointers**: Fast/slow for cycle detection or partitioning
3. **Sorted input scan**: Use sorted order to make directional decisions
4. **Merge-style traversal**: Walk two sorted inputs simultaneously

## Recognition Clues

- Input is sorted (or can be sorted)
- Need pair/triple relationships
- Shrink search space from both ends
- Maintain an invariant while moving pointers
- "Find pair that sums to target" on sorted input

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | ⬜ | Opposite pointers |
| 2 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | ⬜ | Opposite pointers on sorted |
| 3 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | ⬜ | Fix one + two pointer scan |
| 4 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | ⬜ | Greedy shrink |
| 5 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | ⬜ | Left/right max pointers |

## Common Mistakes
- Forgetting to skip duplicates in 3Sum
- Moving the wrong pointer (always move the one that could improve the answer)
- Not handling the empty or single-element case
