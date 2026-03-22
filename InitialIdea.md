# LeetCode Study Plan in Python

## Goal

Build strong pattern recognition for LeetCode interview problems using Python, in an order that matches how problem-solving skills usually develop.

This plan is designed to avoid the common mistake of studying data structures in isolation for too long. Instead, it mixes:

- Python fluency
- common data structures
- high-frequency problem-solving patterns
- advanced paradigms like graphs, backtracking, greedy, and DP

---

## Why the original order needs adjustment

A structure like this:

1. arrays
2. linked lists
3. stacks/queues
4. tree traversal
5. DFS/BFS
6. BST
7. two pointers / sliding window
8. backtracking
9. DP

is not bad, but it delays some of the most useful interview patterns too much.

In practice, **two pointers**, **sliding window**, **hash maps**, and **binary search** appear earlier and more often than linked lists or BST-specific skills.

A better learning path is:

1. learn Python tools for problem solving
2. learn easy, high-frequency patterns early
3. build confidence on medium problems
4. move into deeper recursive/search/optimization topics later

---

# Recommended Learning Order

## 0. Python basics for problem solving

Before serious LeetCode practice, be comfortable with:

- lists and strings
- dictionaries and sets
- loops and `enumerate`
- list comprehensions
- functions
- sorting with `key=...`
- `collections.Counter`
- `collections.defaultdict`
- `collections.deque`
- `heapq`

### Why this comes first
Many LeetCode struggles are not algorithmic. They come from weak Python fluency.

### Practice goals
- write clean loops quickly
- count frequencies with a dictionary or `Counter`
- use sets for O(1) membership checks
- use `deque` for BFS
- use `heapq` for top-k and priority problems

---

## 1. Arrays, strings, hash map, hash set

This should be your first major topic.

### Why
A huge fraction of easy and medium problems are built on:
- arrays
- strings
- frequency counting
- lookups
- sorting
- simple simulation

### Core patterns
- brute force to optimized lookup
- counting/frequency map
- prefix ideas
- sorting-based transformation
- simulation

### Example problems
- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Product of Array Except Self
- Top K Frequent Elements

### What mastery means
You can look at an array/string problem and quickly decide:
- brute force?
- sorting?
- hash map?
- set?
- prefix sum?

---

## 2. Two pointers

This should come very early.

### Why
Two pointers is one of the most common interview patterns and is much more useful early on than linked list manipulation alone.

### Core patterns
- pointers from both ends
- same-direction pointers
- fast/slow pointers
- merge-style scanning

### Example problems
- Valid Palindrome
- Two Sum II
- Squares of a Sorted Array
- 3Sum
- Container With Most Water

### Recognition clues
Use two pointers when:
- input is sorted
- you need pair/triple relationships
- you want to shrink a search space from both ends
- you can maintain an invariant while moving pointers

---

## 3. Sliding window

This is closely related to arrays and two pointers.

### Why
Sliding window solves many substring/subarray problems efficiently.

### Core patterns
- fixed-size window
- variable-size window
- frequency map inside a window
- expand and shrink logic

### Example problems
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Permutation in String
- Find All Anagrams in a String
- Maximum Average Subarray I

### Recognition clues
Use sliding window when:
- the problem asks for a contiguous subarray or substring
- you need longest/shortest valid segment
- you maintain counts while moving boundaries

---

## 4. Stack and queue

Learn these early because they appear in many categories.

### Why
Stacks are common in parsing, monotonic problems, and DFS simulation. Queues are essential for BFS.

### Core patterns
- stack for matching and undo
- monotonic stack
- queue for level-order traversal
- queue for shortest-step exploration in unweighted settings

### Example problems
- Valid Parentheses
- Daily Temperatures
- Next Greater Element
- Implement Queue using Stacks
- Binary Tree Level Order Traversal

### Recognition clues
Use a stack when:
- you need “most recent unmatched item”
- the problem asks for next greater/smaller
- recursive process needs iterative simulation

Use a queue when:
- you process nodes level by level
- you need shortest number of steps in an unweighted graph/grid

---

## 5. Binary search

This should come earlier than many people expect.

### Why
Binary search is not only for sorted arrays. It also teaches “searching over answer space.”

### Core patterns
- classic binary search
- lower bound / upper bound
- search in rotated arrays
- binary search on answer

### Example problems
- Binary Search
- Search Insert Position
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Koko Eating Bananas

### Recognition clues
Use binary search when:
- the search space is ordered
- the answer has a monotonic property
- you can ask: “If x works, do all larger/smaller values also work?”

---

## 6. Linked list

Important, but not one of the earliest topics.

### Why
Linked lists are good for pointer discipline and interview practice, but they appear less broadly than arrays, hash maps, and window patterns.

### Core patterns
- dummy node
- reverse list
- slow/fast pointer
- merge lists
- cycle detection
- split and reconnect

### Example problems
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Remove Nth Node From End of List
- Reorder List

### Recognition clues
Use linked list patterns when:
- pointer rewiring matters more than indexing
- in-place structure changes are central
- you need cycle detection or midpoint finding

---

## 7. Recursion basics

Before advanced trees, graphs, and backtracking, recursion should feel natural.

### Why
Recursion is the mental model behind many tree, graph, DP, and backtracking problems.

### Core ideas
- define a smaller subproblem
- establish base case
- combine recursive results
- trust the recursive contract

### Practice goals
- write recursive DFS for trees
- understand call stack behavior
- return useful information from subproblems

---

## 8. Trees: DFS, BFS, traversals

This is a major stage.

### Why
Tree problems train recursive decomposition very effectively.

### Topics
- preorder, inorder, postorder
- recursive traversal
- iterative traversal with stack
- BFS / level-order traversal
- path-based problems
- subtree-information problems

### Example problems
- Maximum Depth of Binary Tree
- Same Tree
- Invert Binary Tree
- Diameter of Binary Tree
- Binary Tree Level Order Traversal
- Lowest Common Ancestor of a Binary Tree

### Recognition clues
Typical tree questions ask:
- what information should each subtree return?
- do I need DFS or BFS?
- is the answer path-based, level-based, or subtree-based?

---

## 9. Binary Search Tree (BST)

Treat BST as a tree subtopic, not a completely separate phase.

### Why
BST problems are easier after general tree understanding.

### Core patterns
- inorder gives sorted order
- use value ordering to prune search
- validate ordering constraints
- kth smallest via inorder

### Example problems
- Search in a BST
- Validate Binary Search Tree
- Kth Smallest Element in a BST
- Lowest Common Ancestor of a BST

---

## 10. Heap / priority queue

This is missing from many beginner plans, but it is very important.

### Why
Heaps appear in top-k, scheduling, merge-k, and stream problems.

### Core patterns
- min heap
- max heap via negative values
- maintain size-k heap
- repeatedly extract best candidate

### Example problems
- Kth Largest Element in an Array
- Top K Frequent Words
- Merge K Sorted Lists
- Find Median from Data Stream
- Task Scheduler

### Recognition clues
Use a heap when:
- you repeatedly need the smallest/largest item
- you need top-k efficiently
- you process data streams
- merging multiple sorted sources is needed

---

## 11. Graphs

This is one of the biggest categories after trees.

### Why
Many grid problems are really graph problems. BFS/DFS patterns become much more general here.

### Topics
- graph representation
- DFS traversal
- BFS traversal
- connected components
- cycle detection
- topological sort
- union find

### Example problems
- Number of Islands
- Clone Graph
- Course Schedule
- Pacific Atlantic Water Flow
- Rotting Oranges
- Graph Valid Tree

### Recognition clues
Think graph when:
- states are connected
- you can move between nodes/cells
- connectivity matters
- shortest path in an unweighted setting matters
- prerequisite/dependency order matters

---

## 12. Backtracking

Learn this after recursion and trees/graphs.

### Why
Backtracking requires comfort with recursive state exploration.

### Core patterns
- choose
- explore
- unchoose
- prune invalid branches

### Example problems
- Subsets
- Permutations
- Combination Sum
- Word Search
- N-Queens

### Recognition clues
Use backtracking when:
- you need all possible valid combinations
- the search tree branches on decisions
- partial solutions can be extended step by step

---

## 13. Greedy

This is often overlooked, but very common.

### Why
Some medium problems become easy once the greedy invariant is identified.

### Core patterns
- sort and make local optimal choices
- interval scheduling
- maintain a best-so-far choice

### Example problems
- Jump Game
- Gas Station
- Merge Intervals
- Non-overlapping Intervals
- Partition Labels

### Recognition clues
Use greedy when:
- a local choice can be proven safe
- sorting reveals structure
- the problem asks for minimum/maximum with natural ordering

---

## 14. Dynamic programming

Keep DP later.

### Why
DP becomes much easier after you are already comfortable with recursion, memoization, and problem decomposition.

### Learning order inside DP
1. memoization basics
2. 1D DP
3. 2D DP
4. knapsack-style problems
5. subsequence/string DP
6. interval/tree DP

### Example problems
- Climbing Stairs
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence
- Decode Ways

### Recognition clues
Think DP when:
- there are overlapping subproblems
- choices repeat across states
- brute force recursion revisits the same work
- you can define a state and recurrence

---

# Final Recommended Learning Order

1. Python basics for problem solving  
2. Arrays and strings  
3. Hash map and hash set  
4. Two pointers  
5. Sliding window  
6. Stack and queue  
7. Binary search  
8. Linked list  
9. Recursion basics  
10. Trees (DFS, BFS, traversals)  
11. BST  
12. Heap / priority queue  
13. Graphs  
14. Backtracking  
15. Greedy  
16. Dynamic programming  

---

# The Most Important LeetCode Patterns

## Arrays and strings
- brute force to hash optimization
- sorting
- prefix sum
- simulation

## Hashing
- frequency counting
- membership checks
- grouping by key
- tracking seen elements

## Two pointers
- opposite-direction scan
- fast/slow pointers
- partitioning
- merge traversal

## Sliding window
- fixed-size window
- variable-size window
- window frequency maps

## Stack
- matching parentheses
- monotonic stack
- traversal simulation

## Queue / BFS
- level-order traversal
- shortest path in unweighted graph/grid

## Binary search
- sorted search
- lower/upper bound
- binary search on answer

## Linked list
- dummy node
- reversal
- merge
- cycle detection
- split and reconnect

## Trees
- preorder/inorder/postorder
- recursive subtree return
- path computation
- BFS by level

## BST
- value-based pruning
- inorder sorted property

## Heap
- top-k
- running minimum/maximum
- merge-k structures
- stream processing

## Graphs
- DFS/BFS
- connected components
- cycle detection
- topological sort
- union find

## Backtracking
- subsets
- permutations
- combinations
- pruning

## Greedy
- interval scheduling
- sorting + local decision
- proof of local optimality

## Dynamic programming
- state definition
- recurrence
- memoization
- bottom-up transition
- space optimization

---

# How to Study Effectively

## Do not “master” one topic forever before moving on

A common mistake is spending too long trying to perfect one category before touching the next.

Better approach:
- learn the pattern
- solve 5 to 10 selected problems
- review the standard solution
- write a short summary
- move on
- revisit later

This builds pattern recognition faster.

---

## For every problem, do this

1. Identify the topic  
2. Ask what constraints suggest  
3. Think of the brute-force solution first  
4. Ask what makes it too slow  
5. Replace repeated work with a pattern  
6. After solving, record:
   - the pattern used
   - the key trick
   - the time complexity
   - the clue that should help you recognize this pattern next time

---

## Measure progress correctly

Do not define progress as:
- “I solved many random problems”

Define progress as:
- “I can recognize this pattern quickly”
- “I understand why the solution works”
- “I can code it in Python without panic”
- “I know common variations of this pattern”

That is real improvement.

