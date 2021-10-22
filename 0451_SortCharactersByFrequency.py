class Solution:
    # 1st solution
    # O(n) time | O(n) space
    # where n is the total number of the characters
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        result = []
        for k, v in frequency.items():
            result.append(k*v)
        result.sort(key = lambda string: -len(string))
        return "".join(result)