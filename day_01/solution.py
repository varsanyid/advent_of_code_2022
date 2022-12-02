def run(path: str) -> int:
    with open(path, "r") as f:
        calories_sum = build_calories_map(f.readlines())
        print("First part:", solution(calories_sum))
        print("Second part:", solution_2nd_part(calories_sum))

def find_max_key(dictionary: dict[int, int]) -> int:
    max: int = 0
    for key in dictionary:
        if dictionary[key] > dictionary[max]:
            max = key
    return max

def build_calories_map(input: str) -> dict[int, int]:
    calories_sum: dict[int, int] = {}
    counter: int = 0
    for line in input:
        if line == "\n":
            counter += 1
            continue
        if counter not in calories_sum:
            calories_sum[counter] = int(line)
        else:
            calories_sum[counter] += int(line)
    return calories_sum

def solution(calories_sum: dict[int, int]) -> int:
    return calories_sum[find_max_key(calories_sum)]

def solution_2nd_part(calories: dict[int, int]) -> int:
    return sum(sorted(calories.values())[-3:])

run("./day_01/input.txt")