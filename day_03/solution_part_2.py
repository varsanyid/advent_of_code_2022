from functools import reduce
from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase + ascii_uppercase

def run(path: str) -> int:
    with open(path, "r") as f:
        chunks = build_chunks(f.read().split('\n'))
        sum = 0
        for chunk in chunks:
            sum += find_priority(find_duplicates(chunk))
        return sum

def build_chunks(rucksacks: list[str], step = 3) -> list[list[str]]:
    chunks = []
    for line in range(0, len(rucksacks), step):
        chunks.append(rucksacks[line:line + step])
    return chunks

def find_priority(duplicates: set[str]) -> int:
    return reduce(lambda a, b: a + alphabet.index(b) + 1, duplicates, 0)

def find_duplicates(rucksacks: list[str]) -> set[str]:
    sets: list[set[str]] = []
    for rucksack in rucksacks:
        sets.append(set(rucksack))
    return sets[0].intersection(*sets[1:])

if __name__ == '__main__':
    print(run("./day_03/input.txt"))