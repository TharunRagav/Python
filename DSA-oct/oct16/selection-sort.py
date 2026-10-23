def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minele = i

        for j in range(i + 1, n):
            if arr[j] < arr[minele]:
                minele = j

        arr[i], arr[minele] = arr[minele], arr[i]

    return arr