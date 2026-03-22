# ShuaShuaTi - LeetCode Mastery Plan

Deep mastery of DSA patterns through NeetCode 150, with multiple approaches, complexity analysis, and test cases for every problem.

## Learning Order

| # | Topic | Problems | Status |
|---|-------|----------|--------|
| 0 | [Python Toolkit](00_python_toolkit/) | Snippets | ⬜ |
| 1 | [Arrays & Hashing](01_arrays_and_hashing/) | 9 | ⬜ |
| 2 | [Two Pointers](02_two_pointers/) | 5 | ⬜ |
| 3 | [Sliding Window](03_sliding_window/) | 6 | ⬜ |
| 4 | [Stack & Queue](04_stack_and_queue/) | 7 | ⬜ |
| 5 | [Binary Search](05_binary_search/) | 7 | ⬜ |
| 6 | [Linked List](06_linked_list/) | 11 | ⬜ |
| 7 | [Trees](07_trees/) | 15 | ⬜ |
| 8 | [Tries](08_tries/) | 3 | ⬜ |
| 9 | [Heap / Priority Queue](09_heap/) | 7 | ⬜ |
| 10 | [Backtracking](10_backtracking/) | 9 | ⬜ |
| 11 | [Graphs](11_graphs/) | 13 | ⬜ |
| 12 | [Advanced Graphs](12_advanced_graphs/) | 6 | ⬜ |
| 13 | [1D Dynamic Programming](13_one_d_dp/) | 12 | ⬜ |
| 14 | [2D Dynamic Programming](14_two_d_dp/) | 11 | ⬜ |
| 15 | [Greedy](15_greedy/) | 8 | ⬜ |
| 16 | [Intervals](16_intervals/) | 6 | ⬜ |
| 17 | [Math & Geometry](17_math_and_geometry/) | 8 | ⬜ |
| 18 | [Bit Manipulation](18_bit_manipulation/) | 7 | ⬜ |

**Total: ~150 problems**

## Per-Problem Structure

Each problem folder contains:

```
problem_name/
├── solution.py          # Clean solution with inline complexity
├── approaches.md        # Brute → optimal progression with Big-O
└── test_solution.py     # Edge cases + custom tests (pytest)
```

## Study Method

For every problem:

1. **Identify** the topic and pattern
2. **Brute force** first — understand the naive approach
3. **Optimize** — what repeated work can be eliminated?
4. **Code** both iterative and recursive where applicable
5. **Record**: pattern used, key insight, time complexity, recognition clue
6. **Revisit** after 3-7 days

## Setup

```bash
# First time only — install Python and dependencies
uv sync
```

That's it. `uv` handles the virtual environment automatically — no need to activate anything.

## How to Use uv

### Run a solution directly

```bash
uv run python 01_arrays_and_hashing/two_sum/solution.py
```

### Run tests for one problem

```bash
uv run pytest 01_arrays_and_hashing/two_sum/test_solution.py -v
```

### Run all tests in a topic

```bash
uv run pytest 01_arrays_and_hashing/ -v
```

### Run ALL tests in the repo

```bash
uv run pytest -v
```

### Quick tip

`uv run` is the only command you need. It:
- Finds the virtual environment automatically
- Installs any missing dependencies
- Runs your command inside the project environment

No `source .venv/bin/activate` or `pip install` needed.
