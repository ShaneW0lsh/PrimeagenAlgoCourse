class Point:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


directions = [
    [1, 0],  # down
    [0, 1],  # right
    [-1, 0],  # up
    [0, -1]  # left
]


def walk(maze: list[str], wall: str, curr: Point, end: Point,
         seen: list[list[bool]], path: list[Point]) -> bool:
    x_outside_bounds = curr.x < 0 or curr.x > maze[0].__len__()
    y_outside_bounds = curr.y < 0 or curr.y > maze.__len__()
    if x_outside_bounds or y_outside_bounds:
        return False

    if maze[curr.y][curr.x] == wall:
        return False

    if [curr.y, curr.x] == [end.y, end.x]:
        path.append(curr)
        return True

    if seen[curr.y][curr.x]:
        return False

    path.append(curr)
    seen[curr.y][curr.x] = True

    for [y, x] in directions:
        if walk(maze, wall,
                Point(curr.y + y, curr.x + x),
                end, seen, path):
            return True

    path.pop()
    return False


def solve(maze: list[str], wall: str,
          start: Point, end: Point) -> list[Point]:
    path = []
    seen = [[False for i in range(maze[0].__len__())]
            for j in range(maze.__len__())]
    walk(maze, wall, start, end, seen, path)

    return path
