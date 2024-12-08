from pathlib import Path
from itertools import product
import time


class Solution:

    def __init__(self, input_path: str):
        self.input_path = input_path
        self.lines = self._process_input()

    def _process_input(self):
        with open(self.input_path) as input:
            lines = input.read().splitlines()

        return lines

    def _operator(self, total: int, n: int, op: str) -> int:
        if op == "*":
            return total * n
        else:
            return total + n

    def part1(self) -> int | str:
        """Solves part 1 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 1.
        """

        targets = [int(sub[0][:-1]) for sub in (ele.split() for ele in self.lines)]

        value_numbers = [
            [int(a) for a in sub[1:]] for sub in (ele.split() for ele in self.lines)
        ]

        print(len(targets) == len(value_numbers))

        totals = []
        operators = ["+", "*"]
        # iterate over dict - getting target and list of values
        for target, values in zip(targets, value_numbers):

            # iterate over operators to get all possible combinations of
            for opers in product(operators, repeat=len(values[1:])):

                # get first value as start of the operator
                count = values[0]

                # iterate over each operator
                for op, val in zip(opers, values[1:]):

                    count = self._operator(count, val, op)

                    if count > target:
                        break

                if count == target:
                    totals.append(target)
                    break

        return sum(totals)

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
