def bubble_sort(data: list) -> list:
    result = data.copy()
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j+1]:
                tmp = result[j]
                result[j] = result[j+1]
                result[j+1] = tmp
    return result
