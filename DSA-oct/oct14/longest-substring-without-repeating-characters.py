class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        window = {}

        for right in range(len(s)):
            ch = s[right]

            if ch in window and window[ch] >= left:
                left = window[ch] + 1

            window[ch] = right

            length = right - left + 1
            max_length = max(max_length, length)

        return max_length