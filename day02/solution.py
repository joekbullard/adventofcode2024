from pathlib import Path


class Solution:
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.lines = self._process_input()

    def _process_input(self):
        with open(self.input_path) as input:
            lines = input.read().splitlines()

        return lines

    @staticmethod
    def _check_safety(digits: list[int]) -> bool:
        """Iterates over list of ints to determine if list is safe
        or not

        Args:
            digits (list[int]): List of integers to check for safety

        Returns:
            bool: if safe then returns True, else False
        """
        delta = digits[1] - digits[0]
        if 1 <= delta <= 3:
            expected = (1, 2, 3)
        elif -3 <= delta <= -1:
            expected = (-3, -2, -1)
        else:
            return False

        for d in range(1, len(digits) - 1):
            delta = digits[d + 1] - digits[d]
            if delta not in expected:
                return False

        return True

    def part1(self) -> int | str:
        """Solves part 1 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 1.
        """
        count = 0
        for line in self.lines:
            digits = [int(i) for i in line.split()]

            is_safe = self._check_safety(digits)

            if is_safe:
                count += 1

        return count

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """
        count = 0
        for line in self.lines:
            digits = [int(i) for i in line.split()]

            is_safe = self._check_safety(digits)

            if is_safe:
                count += 1
            else:
                for i in range(len(digits)):
                    sub_list = digits[:i] + digits[i + 1 :]
                    is_safe = self._check_safety(sub_list)

                    if is_safe:
                        count += 1
                        break

        return count


input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
