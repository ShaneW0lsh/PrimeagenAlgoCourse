from math import floor, sqrt


def two_crystal_balls(heights: list):
    jump = floor(sqrt(len(heights)))

    saved_index = jump
    for i in range(jump, len(heights), jump):
        saved_index = i
        if heights[i] is True:
            break

    last_position = saved_index - jump
    for i in range(last_position, len(heights)):
        if heights[i] is True:
            return i
    return -1
