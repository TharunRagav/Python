def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, count1 = merge_sort(arr[:mid])
    right, count2 = merge_sort(arr[mid:])

    merged, count3 = merge(left, right)

    return merged, count1 + count2 + count3


def merge(left, right):
    result = []
    i = 0
    j = 0
    count = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            count += len(left) - i
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result, count


arr = [2, 4, 1, 3, 5]

sorted_arr, total = merge_sort(arr)

print("Sorted Array:", sorted_arr)
print("Inversion Count:", total)