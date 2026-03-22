# 14 - 2D Dynamic Programming

Extend 1D DP to two dimensions — grid paths, string matching, and interval problems.

## Core Patterns

1. **Grid DP**: `dp[i][j]` = answer for cell (i, j)
2. **String DP**: `dp[i][j]` = answer for `s1[:i]` and `s2[:j]`
3. **Interval DP**: `dp[i][j]` = answer for subarray `arr[i:j]`
4. **Knapsack 2D**: `dp[i][w]` = answer using first i items with capacity w

## Recognition Clues

- Two strings being compared/matched
- Grid path counting or optimization
- "Longest common subsequence/substring"
- "Edit distance"
- Subproblem depends on two varying indices

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | ⬜ | Grid path counting |
| 2 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | ⬜ | Classic string DP |
| 3 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | ⬜ | State machine DP |
| 4 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | ⬜ | Unbounded knapsack counting |
| 5 | [Target Sum](https://leetcode.com/problems/target-sum/) | Medium | ⬜ | Subset sum variant |
| 6 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | ⬜ | Two-pointer DP |
| 7 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | ⬜ | DFS + memo on grid |
| 8 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard | ⬜ | String matching DP |
| 9 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | ⬜ | Classic string DP |
| 10 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | ⬜ | Interval DP |
| 11 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | ⬜ | String DP with '*' |

## Common Mistakes
- Wrong iteration order in bottom-up (must fill dependencies first)
- String DP: off-by-one between 0-indexed string and 1-indexed dp table
- Forgetting to handle empty string/row base cases
