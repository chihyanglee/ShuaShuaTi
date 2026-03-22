# 18 - Bit Manipulation

XOR tricks, bitmasks, and binary operations.

## Core Patterns

1. **XOR properties**: `a ^ a = 0`, `a ^ 0 = a` — find the unique element
2. **Bitmask**: Use bits to represent subsets or states
3. **Bit counting**: `n & (n-1)` removes lowest set bit
4. **Shift operations**: Multiply/divide by 2, extract bits

## Useful Bit Operations

```python
# Check if bit i is set
(n >> i) & 1

# Set bit i
n | (1 << i)

# Clear bit i
n & ~(1 << i)

# Count set bits
bin(n).count('1')  # or n & (n-1) loop

# Check power of 2
n > 0 and n & (n-1) == 0
```

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | ⬜ | XOR all elements |
| 2 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | ⬜ | n & (n-1) loop |
| 3 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | ⬜ | DP on bits |
| 4 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | ⬜ | Bit-by-bit build |
| 5 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | ⬜ | XOR with indices |
| 6 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | ⬜ | Bit addition |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | ⬜ | Digit extraction |

## Common Mistakes
- Python integers have unlimited width — no overflow, but watch for negative numbers
- XOR: forgetting that it only works when exactly one element is unique
- Signed vs unsigned: Python doesn't have unsigned ints, may need masking
