def frequency_sort(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    arr = list(freq.keys())

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if freq[arr[j]] < freq[arr[min_index]]:
                min_index = j

            elif freq[arr[j]] == freq[arr[min_index]]:
                if arr[j] > arr[min_index]:
                    min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    result = []

    for num in arr:
        result.extend([num] * freq[num])

    return result


nums = [1, 1, 2, 2, 2, 3]
print(frequency_sort(nums))