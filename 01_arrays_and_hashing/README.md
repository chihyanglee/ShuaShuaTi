# 01 - Arrays and Hashing

The foundation. A huge fraction of easy and medium problems are built on arrays, strings, frequency counting, and hash lookups.

## Core Patterns

1. **Brute force → hash optimization**: Replace O(n²) nested loops with O(n) hash lookups
2. **Frequency counting**: Use Counter/dict to track element counts
3. **Prefix sum**: Precompute cumulative sums for range queries
4. **Sorting-based transformation**: Sort to reveal structure
5. **Index as hash key**: Use array indices for O(1) mapping
6. **Grouping by key**: defaultdict(list) to group elements

## Recognition Clues

- "Find a pair/element that satisfies..." → hash map
- "Count occurrences..." → Counter
- "Sum of subarray..." → prefix sum
- "Group elements by..." → defaultdict
- "Check if duplicate/anagram..." → set or Counter

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | ⬜ | Set membership |
| 2 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | ⬜ | Frequency count |
| 3 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | ⬜ | Hash map complement |
| 4 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | ⬜ | Sorted key grouping |
| 5 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | ⬜ | Bucket sort / heap |
| 6 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | ⬜ | Delimiter design |
| 7 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | ⬜ | Prefix/suffix product |
| 8 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | ⬜ | Set per row/col/box |
| 9 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | ⬜ | Set + sequence start |

## Common Mistakes
- Forgetting that Python strings are immutable — use `list` for char manipulation
- Off-by-one in prefix sum (index 0 is usually a sentinel)
- Not handling empty input
