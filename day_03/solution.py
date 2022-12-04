from functools import reduce
from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase + ascii_uppercase

def run(path: str) -> int:
    with open(path, "r") as f:
        priorities = list(map(lambda line: find_priority(find_duplicates(line)), f.read().split('\n')))
        return sum(priorities)

def find_priority(duplicates: set[str]) -> int:
    return reduce(lambda a, b: a + alphabet.index(b) + 1, duplicates, 0)

def find_duplicates(rucksack: str) -> set[str]:
    middle = int(len(rucksack) / 2)
    begin = rucksack[:middle]
    end = rucksack[middle:]
    results = set()
    for x in begin:
        for y in end:
            if x == y:
                results.add(x)
                break
    return results

if __name__ == '__main__':
    print(run("./day_03/input.txt"))