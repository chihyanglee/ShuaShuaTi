# 03 - Sliding Window

Efficiently process contiguous subarrays/substrings by expanding and shrinking a window.

## Core Patterns

1. **Fixed-size window**: Window size is given, slide it across
2. **Variable-size window**: Expand right, shrink left when condition breaks
3. **Frequency map in window**: Track char/element counts within window
4. **Expand-shrink logic**: `right` always moves; `left` moves when invalid

## Recognition Clues

- "Contiguous subarray/substring"
- "Longest/shortest valid segment"
- "At most k distinct elements"
- Maintaining counts while moving boundaries
- Optimization over all subarrays of some property

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | ⬜ | Track min so far |
| 2 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | ⬜ | Variable window + set |
| 3 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | ⬜ | Window + max freq |
| 4 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | ⬜ | Fixed window + freq match |
| 5 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | ⬜ | Variable window + freq map |
| 6 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | ⬜ | Monotonic deque |

## Common Mistakes
- Forgetting to shrink the window (infinite expansion)
- Off-by-one when calculating window size (`right - left + 1`)
- Not updating frequency map when shrinking
