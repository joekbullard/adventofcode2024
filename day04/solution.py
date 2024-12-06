from pathlib import Path


class Solution:

    def __init__(self, input_path: str):
        self.input_path = input_path
        self.lines = self._process_input()

    def _process_input(self):
        with open(self.input_path) as input:
            lines = input.read().splitlines()

        return lines

    def _search(self, sequence, direction, origin_x, origin_y, index=0) -> int:

        if index >= len(sequence):  # Entire sequence matched
            print("xmas found")
            return True

        x_diff, y_diff = direction
        loc_x = origin_x + x_diff
        loc_y = origin_y + y_diff

        if (
            loc_x < 0
            or loc_y < 0
            or loc_y >= len(self.lines)
            or loc_x >= len(self.lines[loc_y])
        ):
            return False

        if self.lines[loc_y][loc_x] == sequence[index]:
            return self._search(sequence, direction, loc_x, loc_y, index + 1)

        return False

    def part1(self) -> int | str:
        """Solves part 1 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 1.
        """

        directions = (
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        )
        total = 0
        for count_y, row in enumerate(self.lines):
            for col in range(len(row)):
                current_char = self.lines[count_y][col]
                if current_char == "X":
                    for dir in directions:
                        count = self._search("MAS", dir, col, count_y)
                        if count:
                            total += 1

        return total

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """
        MASSAM = ("MAS", "SAM")

        count = 0
        for y, line in enumerate(self.lines[1:-1], 1):
            for x, char in enumerate(line[1:-1], 1):
                if char == "A":
                    top_right = self.lines[y - 1][x + 1]
                    bottom_left = self.lines[y + 1][x - 1]
                    bottom_right = self.lines[y + 1][x + 1]
                    top_left = self.lines[y - 1][x - 1]
                    if (
                        top_right + char + bottom_left in MASSAM
                        and top_left + char + bottom_right in MASSAM
                    ):
                        count += 1

        return count


input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
