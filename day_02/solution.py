from abc import abstractmethod

class Shape:
    def __init__(self, sign, encrypted, score) -> None:
        self.sign = sign
        self.encrypted = encrypted
        self.score = score
    
    @abstractmethod
    def compare(this: 'Shape', other: 'Shape'):
        pass

class Rock(Shape):
    def __init__(self) -> None:
        super().__init__(sign = "A", encrypted = "X", score = 1)

    def compare(this: 'Shape', other: 'Shape'):
        if isinstance(other, Paper):
            return -1
        elif isinstance(other, Scissor):
            return 1
        else:
            return 0

class Paper(Shape):
    def __init__(self) -> None:
        super().__init__(sign = "B", encrypted = "Y", score = 2)
    
    def compare(this: 'Shape', other: 'Shape'):
        if isinstance(other, Rock):
            return 1
        elif isinstance(other, Scissor):
            return -1
        else:
            return 0

class Scissor(Shape):
    def __init__(self) -> None:
        super().__init__(sign = "C", encrypted = "Z", score = 3)
    
    def compare(this: 'Shape', other: 'Shape'):
        if isinstance(other, Paper):
            return 1
        elif isinstance(other, Rock):
            return -1
        else:
            return 0

def get_shape(letter: str) -> Shape:
    if letter == 'A' or letter == 'X':
        return Rock()
    elif letter == 'B' or letter == 'Y':
        return Paper()
    else:
        return Scissor()

def run(path: str) -> int:
    with open(path, "r") as f:
        score = 0
        for line in f.read().split("\n"):
            shapes: list[str] = line.split(" ")
            left: Shape = get_shape(shapes[0])
            right: Shape = get_shape(shapes[1])
            result = right.compare(left)
            if result == 1:
                score += 6
            elif result == 0:
                score += 3
            score += right.score
        return score

run("./day_02/input.txt")