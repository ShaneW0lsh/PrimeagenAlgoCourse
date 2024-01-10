def binary_search(haystack: list[int], needle: int) -> int:
    left = 0
    right = len(haystack)
    while left < right:
        middle = left + (right - left) // 2
        if haystack[middle] == needle:
            return middle
        elif haystack[middle] > needle:
            right = middle
        else:
            left = middle + 1
    return -1
