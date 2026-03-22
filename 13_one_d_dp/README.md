# 13 - 1D Dynamic Programming

Start DP here. Define state, write recurrence, optimize space.

## Core Patterns

1. **Linear DP**: `dp[i]` depends on previous elements
2. **Decision DP**: At each step, choose to take or skip
3. **Counting DP**: Number of ways to reach a state
4. **Optimization DP**: Min/max cost to reach a state

## Learning Order Inside DP

1. Memoization (top-down) — easiest to start with
2. Bottom-up tabulation — convert memo to iterative
3. Space optimization — reduce from O(n) to O(1) when possible

## Recognition Clues

- Overlapping subproblems
- "Number of ways to..."
- "Minimum/maximum cost to..."
- Brute force recursion revisits same states
- Can define `dp[i]` = answer for first i elements

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | ⬜ | Fibonacci-style |
| 2 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | ⬜ | Min of two prev |
| 3 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | ⬜ | Take or skip |
| 4 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | ⬜ | Circular → two passes |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | ⬜ | Expand from center |
| 6 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | ⬜ | Expand from center |
| 7 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | ⬜ | Counting with constraints |
| 8 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | ⬜ | Unbounded knapsack |
| 9 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | ⬜ | Track min AND max |
| 10 | [Word Break](https://leetcode.com/problems/word-break/) | Medium | ⬜ | Prefix matching DP |
| 11 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | ⬜ | Classic LIS |
| 12 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | ⬜ | 0/1 knapsack |

## Common Mistakes
- Not identifying the right state — start by asking "what do I need to know at position i?"
- Forgetting base cases
- Off-by-one in bottom-up iteration direction
- Maximum Product: forgetting that negative × negative = positive
