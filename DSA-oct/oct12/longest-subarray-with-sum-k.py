def longestSubarray(nums, k):
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1

        if window_sum == k:
            max_length = max(max_length, right - left + 1)

    return max_length