from pathlib import Path


class Solution:

    def __init__(self, input_path: str):
        self.input_path = input_path
        self.line = self._process_input()

    def _process_input(self):
        with open(self.input_path) as input:
            line = input.readline()

        return line

    def part1(self) -> int | str:
        """Solves part 1 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 1.
        """

        index_list = [
            "." if i % 2 == 1 else int(i / 2)
            for i in range(len(self.line))
            for _ in range(int(self.line[i]))
        ]

        n = len(index_list)

        j = 0
        i = 0
        total = 0

        while i < (n - j):
            if index_list[i] == ".":
                while i < (n - 1 - j):
                    if isinstance(index_list[n - 1 - j], int):
                        index_list[i], index_list[n - 1 - j] = (
                            index_list[n - 1 - j],
                            index_list[i],
                        )
                        j += 1
                        break
                    j += 1
            total += i * index_list[i]
            i += 1

        return total

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """

        return 0


input_path = Path(__file__).parent / "example.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
