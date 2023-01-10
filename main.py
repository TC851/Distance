def min_distance(arr):
    min_distance = 0
    min_index = 0
    for i in range(len(arr) - 1):
        distance = abs(arr[i] - arr[i + 1])
        if distance > min_distance:
            min_distance = distance
            min_index = i
    return min_index


# Path: main.py_____________________________________________
arr = [1, 3, 11, 9, 7, 12]
output = min_distance(arr)
print(output)                # print index
