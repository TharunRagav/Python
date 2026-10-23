class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        chars = list(freq.keys())
        n = len(chars)

        for i in range(n):
            max_index = i

            for j in range(i + 1, n):
                if freq[chars[j]] > freq[chars[max_index]]:
                    max_index = j

            chars[i], chars[max_index] = chars[max_index], chars[i]

        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result