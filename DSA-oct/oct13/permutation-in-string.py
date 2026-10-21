class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}

        for ch in s1:
            target[ch] = target.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1

            if right - left + 1 > len(s1):
                old = s2[left]
                window[old] -= 1

                if window[old] == 0:
                    del window[old]

                left += 1

            if window == target:
                return True

        return False