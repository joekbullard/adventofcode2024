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
        rules = [(int(x.split('|')[0]), int(x.split('|')[1])) for x in self.lines[:21]]
       
        updates = [[int(num) for num in group.split(",")] for group in self.lines[22:]]

        total = 0
        
        for update in updates:
            include = True
            for rule in rules:
                left, right = rule
                try:
                    left_idx = update.index(left)
                    try:
                        right_idx = update.index(right)
                        if left_idx > right_idx:
                            include = False
                            break
                    except ValueError:
                        pass
                except ValueError:
                    pass
            if include:
                middle_idx = len(update)//2
                total += update[middle_idx]

            
        return total

            





        return 0
    def part2(self) -> int | str:
        """Solves part 2 of the challenge using the provided input.

        Args:
            input_lines (list[str]): List of lines from input.txt

        Returns:
            int | str: The answer to part 2.
        """
        
        rules = [(int(x.split('|')[0]), int(x.split('|')[1])) for x in self.lines[:21]]
       
        updates = [[int(num) for num in group.split(",")] for group in self.lines[23:]]

        total = 0
        
        for update in updates:
            include = False
            for rule in rules:
                left, right = rule
                try:
                    left_idx = update.index(left)
                    try:
                        right_idx = update.index(right)
                        if left_idx > right_idx:
                            left_value = update.pop(left_idx)
                            new_position = right_idx - 2
                            update.insert(new_position, left_value)
                            include = True
                    except ValueError:
                        pass
                except ValueError:
                    pass
            if include:
                print(update)
                middle_idx = len(update)//2
                total += update[middle_idx]

            
        return total
    

input_path = Path(__file__).parent / "example.txt"
solution = Solution(input_path)

print(f"Solution to part 1: {solution.part1()}")
print(f"Solution to part 2: {solution.part2()}")
