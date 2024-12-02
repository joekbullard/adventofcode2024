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
        safe = True

        for d in range(len(digits) - 1):

            delta = digits[d] - digits[d + 1]
            if d == 0:
                if 1 <= delta <= 3:
                    expected = range(1, 4)
                    continue
                elif -3 <= delta < 0:
                    expected = range(-3, 0)
                    continue
                else:
                    safe = False
                    break
            if delta not in expected:
                safe = False
                break
        return safe

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
