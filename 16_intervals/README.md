# 16 - Intervals

Interval problems are common enough to treat as their own category.

## Core Patterns

1. **Sort by start**: Standard for merge/insert
2. **Sort by end**: Optimal for scheduling (maximize non-overlapping)
3. **Sweep line**: Process events (start/end) in order
4. **Overlap detection**: Two intervals overlap if `a.start < b.end and b.start < a.end`

## Recognition Clues

- "Merge overlapping intervals"
- "Find non-overlapping / minimum removal"
- "Meeting rooms" / scheduling
- "Insert interval into sorted list"

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | ⬜ | Merge on overlap |
| 2 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | ⬜ | Sort + merge adjacent |
| 3 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | ⬜ | Sort by end, greedy remove |
| 4 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy | ⬜ | Sort + overlap check |
| 5 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | ⬜ | Min heap / sweep line |
| 6 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard | ⬜ | Sort + heap |

## Common Mistakes
- Sorting by start when you should sort by end (or vice versa)
- Off-by-one in overlap condition (inclusive vs exclusive bounds)
- Not handling the case where new interval goes at the very beginning/end
