
from queue import Queue
import re

def run(path: str) -> int:
    with open(path, "r") as f:
        lines = f.read().splitlines()
        stacks = build_stacks(lines)
        for command in lines[10:]:
            move_command(command, stacks)
        for stack in stacks:
            print(stack.get())
        

def move_command(line: str, stacks: list[Queue]) -> None:
    print(line)
    digits = re.findall(r'\d+', line)
    amount = int(digits[0])
    from_stack = int(digits[1])
    to_stack = int(digits[2])
    for _ in range(amount):
        popped = stacks[from_stack - 1].get()
        stacks[to_stack - 1].put(popped)

def build_stacks(lines: list[str]) -> list[Queue]:
    stacks: list[Queue] = []
    for _ in range(9):
        stacks.append(Queue())
    for idx, line in enumerate(lines):
            stack_index = 0
            for char in range(2, len(line), 4):
                if idx < 8:
                    current = line[char - 1]
                    if not current == ' ':
                        stacks[stack_index].put(current)
                    stack_index += 1
                else:
                    break
    return stacks

if __name__ == '__main__':
    run("./day_05/input.txt")