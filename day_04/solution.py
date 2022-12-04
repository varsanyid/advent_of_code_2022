class SectionRange:
    def __init__(self, text: str) -> None:
        halves = text.split("-")
        self.start = int(halves[0])
        self.end = int(halves[1])
        self.range = range(self.start, self.end)
    
    def is_within(self, other: 'SectionRange') -> bool:
        return self.start >= other.start and self.end <= other.end

def run(path: str) -> int:
    with open(path, "r") as f:
        rows = f.read().split('\n')
        counter = 0
        for row in rows:
            sections = row.split(',')
            first = SectionRange(sections[0])
            second = SectionRange(sections[1])
            if first.is_within(second) or second.is_within(first):
                counter += 1
        return counter

if __name__ == '__main__':
    print(run("./day_04/input.txt"))