# 10 - Backtracking

Systematic exploration of all possibilities with pruning. Requires comfort with recursion.

## Core Patterns

1. **Choose → Explore → Unchoose**: The backtracking template
2. **Subsets**: Include or exclude each element
3. **Permutations**: Try each unused element at each position
4. **Combinations**: Choose k from n with ordering constraints
5. **Constraint satisfaction**: Prune invalid branches early

## Backtracking Template

```python
def backtrack(candidates, path, result, start):
    if is_valid(path):       # Base case: found a solution
        result.append(path[:])
        return

    for i in range(start, len(candidates)):
        # Pruning
        if not is_promising(candidates[i]):
            continue

        path.append(candidates[i])        # Choose
        backtrack(candidates, path, result, i + 1)  # Explore
        path.pop()                         # Unchoose
```

## Recognition Clues

- "All possible combinations/permutations/subsets"
- "Find all valid configurations"
- Search tree branches on decisions
- Partial solutions can be extended step by step

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | ⬜ | Include/exclude |
| 2 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | ⬜ | Reuse allowed |
| 3 | [Permutations](https://leetcode.com/problems/permutations/) | Medium | ⬜ | Used array |
| 4 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | ⬜ | Skip duplicates |
| 5 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | ⬜ | Sort + skip dupes |
| 6 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | ⬜ | Grid backtracking |
| 7 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | ⬜ | Partition + check |
| 8 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | ⬜ | Map + backtrack |
| 9 | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | ⬜ | Column/diagonal sets |

## Common Mistakes
- Forgetting to unchoose (pop) after recursive call
- Appending `path` directly instead of `path[:]` (reference vs copy)
- Not sorting before skipping duplicates
- Wrong `start` index: `i` (no reuse) vs `i+1` vs `start`
