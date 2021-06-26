class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))

    # 2nd solution, Divide And Conquer
    # O(n^2) time | O(n) space
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringUtil(s, 0, len(s), k)
    
    def longestSubstringUtil(self, s, start, end, k):
        if end < k:
            return 0
        countMap = collections.Counter(s[start:end])
        for mid in range(start, end):
            if countMap[s[mid]] >= k:
                continue
            midNext = mid + 1
            while midNext < end and countMap[s[midNext]] < k:
                midNext += 1
            return max(self.longestSubstringUtil(s, start, mid, k), \
                       self.longestSubstringUtil(s, midNext, end, k))
        return end - start
