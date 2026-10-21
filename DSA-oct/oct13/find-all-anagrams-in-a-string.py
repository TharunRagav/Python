class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        window = {}
        target = {}

        for ch in p:
            target[ch] = target.get(ch, 0) + 1

        left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if right - left + 1 > len(p):
                old = s[left]
                window[old] -= 1

                if window[old] == 0:
                    del window[old]

                left += 1

            if window == target:
                result.append(left)

        return result