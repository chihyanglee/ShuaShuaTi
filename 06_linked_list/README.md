# 06 - Linked List

Good for pointer discipline. Practice both **iterative** and **recursive** solutions for every problem.

## Core Patterns

1. **Dummy node**: Simplify head-insertion edge cases
2. **Reverse list**: Iterative (prev/curr/next) and recursive
3. **Fast/slow pointer**: Midpoint, cycle detection
4. **Merge lists**: Two-pointer merge
5. **Split and reconnect**: Reorder, partition

## Recognition Clues

- Pointer rewiring matters more than indexing
- In-place structure changes are central
- Cycle detection or midpoint finding needed
- "Reverse", "merge", "reorder" in problem title

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | ⬜ | Iterative + recursive |
| 2 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | ⬜ | Dummy node merge |
| 3 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | ⬜ | Fast/slow pointer |
| 4 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | ⬜ | Find mid + reverse + merge |
| 5 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | ⬜ | Two pointers with gap |
| 6 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | ⬜ | Hash map clone |
| 7 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | ⬜ | Digit-by-digit carry |
| 8 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | ⬜ | Floyd's cycle |
| 9 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | ⬜ | Doubly linked list + hash |
| 10 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | ⬜ | Heap + merge |
| 11 | [Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | ⬜ | Group reverse |

## Important: Iterative vs Recursive

For **every** linked list problem, practice BOTH approaches:
- **Iterative**: Use prev/curr/next pointers, explicit loops
- **Recursive**: Think of the recursive contract — what does the function return for the rest of the list?

## Common Mistakes
- Losing reference to next node before rewiring
- Forgetting to handle `None` / empty list
- Not using dummy node when the head might change
