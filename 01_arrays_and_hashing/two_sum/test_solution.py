"""
Tests for: Two Sum
Run: uv run pytest 01_arrays_and_hashing/two_sum/test_solution.py -v
"""

from solution import Solution


class TestTwoSum:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        assert self.sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test_basic_2(self):
        assert self.sol.twoSum([3, 2, 4], 6) == [1, 2]

    def test_same_element(self):
        assert self.sol.twoSum([3, 3], 6) == [0, 1]

    def test_negative(self):
        assert self.sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_zero(self):
        assert self.sol.twoSum([0, 4, 3, 0], 0) == [0, 3]
