from pathlib import Path
from solution import Solution


def test_part1():
    input_path = Path(__file__).parent / 'example.txt'
    solution = Solution(input_path)
    assert solution.part1() == 1


def test_part2():
    input_path = Path(__file__).parent / 'example.txt'
    solution = Solution(input_path)
    assert solution.part2() == 1
