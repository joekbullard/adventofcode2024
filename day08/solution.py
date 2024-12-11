from pathlib import Path
from itertools import combinations
from typing import Tuple


class Solution:

    def __init__(self, input_path: str):
        self.input_path = input_path
        self.lines = self._process_input()

    def _process_input(self):
        with open(self.input_path) as input:
            lines = input.read().splitlines()

        return lines

    def _calc_diff(
        self, coord_a: Tuple[int, int], coord_b: Tuple[int, int]
    ) -> Tuple[int, int]:
        y_diff = coord_a[0] - coord_b[0]
        x_diff = coord_a[1] - coord_b[1]
        return (y_diff, x_diff)

    def part1(self) -> int | str:
        """Solves part 1 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 1.
        """

        hash_table = {}

        for y, row in enumerate(self.lines):
            for x, char in enumerate(row):
                if char != ".":

                    if char in hash_table:
                        hash_table[char].append((y, x))
                    else:
                        hash_table[char] = [(y, x)]

        values = [list(combinations(value, 2)) for value in hash_table.values()]

        antinodes = []

        for val in values:
            for coord_pairs in val:
                coord_1, coord_2 = coord_pairs
                y_diff, x_diff = self._calc_diff(coord_1, coord_2)
                upper = (coord_1[0] + y_diff, coord_1[1] + x_diff)
                lower = (coord_2[0] - y_diff, coord_2[1] - x_diff)
                if 0 <= upper[0] < len(self.lines) and 0 <= upper[1] < len(
                    self.lines[0]
                ):
                    antinodes.append(upper)
                if 0 <= lower[0] < len(self.lines) and 0 <= lower[1] < len(
                    self.lines[0]
                ):
                    antinodes.append(lower)

        return len(set(antinodes))

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """

        hash_table = {}

        for y, row in enumerate(self.lines):
            for x, char in enumerate(row):
                if char != ".":
                    if char in hash_table:
                        hash_table[char].append((y, x))
                    else:
                        hash_table[char] = [(y, x)]

        values = [list(combinations(value, 2)) for value in hash_table.values()]

        antinodes = []

        size = len(self.lines)

        for val in values:
            for coord_pairs in val:
                coord_a, coord_b = coord_pairs

                y_diff, x_diff = self._calc_diff(coord_a, coord_b)

                while any(0 <= value < size for value in coord_a + coord_b):
                    if 0 <= coord_a[0] < size and 0 <= coord_a[1] < size:
                        antinodes.append(coord_a)
                    if 0 <= coord_b[0] < size and 0 <= coord_b[1] < size:
                        antinodes.append(coord_b)
                    coord_a = (coord_a[0] + y_diff, coord_a[1] + x_diff)
                    coord_b = (coord_b[0] - y_diff, coord_b[1] - x_diff)

        return len(set(antinodes))


input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
