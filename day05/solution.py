from pathlib import Path


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
        rules = [(int(x.split("|")[0]), int(x.split("|")[1])) for x in self.lines[:1176]]

        updates = [[int(num) for num in group.split(",")] for group in self.lines[1178:]]

        total = 0

        for update in updates:
            include = True
            for rule in rules:
                left, right = rule
                if left in update and right in update:
                    left_idx, right_idx = update.index(left), update.index(right)
                    if left_idx > right_idx:
                        include = False
            if include:
                middle_idx = len(update) // 2
                total += update[middle_idx]

        return total

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """

        rules = [(int(x.split("|")[0]), int(x.split("|")[1])) for x in self.lines[:1176]]

        updates = [[int(num) for num in group.split(",")] for group in self.lines[1177:]]

        total = 0
        
        for update in updates:
            include = False
            i = 0
            while i < len(rules):
                left, right = rules[i]
                if left in update and right in update:
                    left_idx, right_idx = update.index(left), update.index(right)
                    if left_idx > right_idx:
                        include = True
                        element = update.pop(left_idx)
                        new_pos = right_idx
                        update.insert(new_pos, element)
                        i = 0
                        continue
                i+=1
            if include:
                middle_idx = len(update) // 2
                total += update[middle_idx]

        return total


input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
