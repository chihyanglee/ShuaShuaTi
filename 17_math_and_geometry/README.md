# 17 - Math and Geometry

Math tricks and matrix operations that show up in interviews.

## Core Patterns

1. **Modular arithmetic**: Remainders, GCD, power mod
2. **Matrix rotation/spiral**: In-place transforms
3. **Digit manipulation**: Reverse, palindrome check
4. **Bit counting**: Powers of two, Hamming weight

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | ⬜ | Transpose + reverse |
| 2 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | ⬜ | Boundary shrinking |
| 3 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | ⬜ | Use first row/col as flags |
| 4 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | ⬜ | Cycle detection |
| 5 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy | ⬜ | Carry propagation |
| 6 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | ⬜ | Fast exponentiation |
| 7 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium | ⬜ | Digit-by-digit multiply |
| 8 | [Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | ⬜ | Hash map of points |

## Common Mistakes
- Integer overflow (Python handles big ints, but watch for negative edge cases)
- Matrix rotation: confusing row/col indices after transpose
- Spiral: boundary variable management
