from pathlib import Path
from day02.solution import Solution

def test_part1():
    input_path = Path(__file__).parent / 'example.txt'
    solution = Solution(input_path)
    assert solution.part1() == 2

def test_part2():
    input_path = Path(__file__).parent / 'example.txt'
    solution = Solution(input_path)
    assert solution.part2() == 4
