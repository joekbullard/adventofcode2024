from pathlib import Path
from collections import Counter


class Solution:
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.lines = self._process_input()

    def _process_input(self):
        with open(self.input_path) as input:
            lines = input.read().splitlines()

        return lines

    def part1(self) -> int | str:
        """Solves part 1 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 1.
        """
        left_list, right_list = [], []

        for line in self.lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

        left_list.sort()
        right_list.sort()

        total = sum([abs(right - left) for right, left in zip(left_list, right_list)])

        return total

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """

        left_list, right_list = [], []
        for line in self.lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

        value_count = {}
        for value in right_list:
            value_count[value] = value_count.get(value, 0) + 1

        total = sum(n * value_count.get(n, 0) for n in left_list)

        return total


input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
