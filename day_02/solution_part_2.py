class Node:
    def __init__(self, text: str, value: int, node: 'Node' = None) -> None:
        self.text = text
        self.value = value
        self.node = node

rock = Node("A", 1)
paper = Node("B", 2, rock)
scissor = Node("C", 3, paper)
rock.node = scissor

def find_parent(parent: Node) -> int:
    text = parent.text
    def loop(node: Node, text: str) -> Node:
        if node.node.text == text:
            return node
        else:
            return loop(node.node, text)
    return loop(parent, text).value

def get_shape(text: str) -> Node:
    if text == 'A':
        return rock
    elif text == 'B':
        return paper
    else:
        return scissor

def run(path: str) -> int:
    with open(path, "r") as f:
        score = 0
        for line in f.read().split("\n"):
            shapes = line.split(" ")
            result = shapes[1]
            node = get_shape(shapes[0])
            addition = 0
            if result == 'X':
                addition += node.node.value
            elif result == 'Y':
                addition += node.value
                addition += 3
            else:
                addition += find_parent(node)
                addition += 6
            score += addition
        return score

print(run("./day_02/input.txt"))