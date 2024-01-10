from recursion.path_finding import solve, Point


def main():
    maze = [
        "########## #",
        "#        # #",
        "#        # #",
        "# ######## #",
        "#          #",
        "# ##########",
    ]

    points = solve(maze, wall="#", start=Point(0, 10), end=Point(5, 1))
    for point in points:
        print(point.y, point.x)


if __name__ == "__main__":
    main()
