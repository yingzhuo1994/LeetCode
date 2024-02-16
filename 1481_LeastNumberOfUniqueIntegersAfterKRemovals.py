class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        freqs = list(counts.values())
        freqs.sort()
        for i, freq in enumerate(freqs):
            if k > freq:
                k -= freq
            elif k == freq:
                return len(freqs) - (i + 1)
            else:
                return len(freqs) - i
        return 0

