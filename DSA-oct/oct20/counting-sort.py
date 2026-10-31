def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_num = max(arr)

    count = [0] * (max_num + 1)

    for num in arr:
        count[num] += 1

    result = []

    for num in range(len(count)):
        while count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result


arr = [4, 2, 2, 8, 3, 3, 1]

print(counting_sort(arr))