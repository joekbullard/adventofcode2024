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
    
    def _calc_diff(self, coord_a: Tuple[int, int], coord_b: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        y_diff = coord_a[0] - coord_b[0]
        x_diff = coord_a[1] - coord_b[1]
        upper = (coord_a[0] + y_diff, coord_a[1] + x_diff)
        lower = (coord_b[0] - y_diff, coord_b[1] - x_diff)
        return upper, lower

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
                if char != '.':
                    
                    if char in hash_table:
                        hash_table[char].append((y, x))
                    else:
                        hash_table[char] = [(y, x)]

        values = [list(combinations(value, 2)) for value in hash_table.values()]

        antinodes = []

        for val in values:
            for coord_pairs in val:
                coord_1, coord_2 = coord_pairs
                upper, lower = self._calc_diff(coord_1, coord_2)
                if 0 <= upper[0] < 50 and 0 <= upper[1] < 50:
                    antinodes.append(upper)
                if 0 <= lower[0] < 50 and 0 <= lower[1] < 50:
                    antinodes.append(lower)

        return len(set(antinodes))

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """

        return 0
    

input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
