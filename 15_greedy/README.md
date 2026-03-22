# 15 - Greedy

Make the locally optimal choice at each step. The trick is proving the greedy choice is safe.

## Core Patterns

1. **Sort and process**: Sort by some criterion, then make greedy decisions
2. **Interval scheduling**: Sort by end time, pick non-overlapping
3. **Track best-so-far**: Maintain a running best as you scan
4. **Proof by exchange**: Show that any other choice isn't better

## Recognition Clues

- A local choice can be proven globally safe
- Sorting reveals structure
- "Minimum/maximum with natural ordering"
- Interval problems (merge, schedule)
- "Can you reach the end?" / "minimum jumps"

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | ⬜ | Kadane's algorithm |
| 2 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | ⬜ | Track max reach |
| 3 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | ⬜ | BFS-style layers |
| 4 | [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | ⬜ | Reset start on deficit |
| 5 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | ⬜ | Counter + greedy group |
| 6 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | ⬜ | Filter + check |
| 7 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | ⬜ | Last occurrence tracking |
| 8 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | ⬜ | Range tracking |

## Common Mistakes
- Assuming greedy works without proof (test with counterexamples first)
- Not sorting when order matters
- Kadane's: forgetting to reset when running sum goes negative
