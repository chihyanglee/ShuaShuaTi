"""
Root conftest.py — allows pytest to import solution.py from any problem folder.

When you run: uv run pytest 01_arrays_and_hashing/two_sum/test_solution.py
pytest adds that folder to sys.path so `from solution import Solution` works.
"""

import sys
from pathlib import Path


def pytest_collect_file(parent, file_path):
    """Ensure each test file's directory is on sys.path for local imports."""
    if file_path.name.startswith("test_") and file_path.suffix == ".py":
        test_dir = str(file_path.parent)
        if test_dir not in sys.path:
            sys.path.insert(0, test_dir)
