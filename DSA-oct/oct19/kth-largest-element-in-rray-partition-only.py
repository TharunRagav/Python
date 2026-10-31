def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    return i + 1


def find_kth_largest(nums, k):
    target = len(nums) - k

    low = 0
    high = len(nums) - 1

    while low <= high:

        p = partition(nums, low, high)

        if p == target:
            return nums[p]

        elif p < target:
            low = p + 1

        else:
            high = p - 1


nums = [3, 2, 1, 5, 6, 4]
k = 2

print(find_kth_largest(nums, k))