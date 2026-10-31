def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


nums = [2, 4, 6, 8, 10, 12, 14]
target = 10

print(binary_search(nums, target))