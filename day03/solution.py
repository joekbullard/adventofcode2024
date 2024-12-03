from pathlib import Path
import re

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
        total = 0
        expression = "mul\(\d{1,3},\d{1,3}\)"
        for line in self.lines:
            matches = re.findall(expression, line)

            for m in matches:
                val_1, val_2 = m[4:-1].split(',')
                total += int(val_1) * int(val_2)

        return total

    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """
        concat_line = []
        for line in self.lines:
            concat_line.extend(line)

        string_line = ''.join(concat_line)

        sections_pattern = r"^.*?don't\(\)|do\(\).*?don't\(\)|do\(\).*$"
        sections = re.findall(sections_pattern, string_line)

        # Step 2: Extract all mul(x, y) patterns from each section
        mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
        total = 0
        for section in sections:
            matches = re.findall(mul_pattern, section)
            for m in matches:
                val_1, val_2 = m[4:-1].split(',')
                total += int(val_1) * int(val_2)
        
        return total
    
            


    

input_path = Path(__file__).parent / "input.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
