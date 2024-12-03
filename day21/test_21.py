from pathlib import Path
import pytest
from .solution import Solution


@pytest.mark.skip(reason="Function not implemented yet")
def test_part1():
    input_path = Path(__file__).parent / "example.txt"
    solution = Solution(input_path)
    assert solution.part1() == 1


@pytest.mark.skip(reason="Function not implemented yet")
def test_part2():
    input_path = Path(__file__).parent / "example.txt"
    solution = Solution(input_path)
    assert solution.part2() == 1
