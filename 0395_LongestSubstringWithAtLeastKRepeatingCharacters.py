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

    # 3rd solution, Sliding Window
    # O(n) time | O(1) space
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique = self.getMaxUniqueLetters(s)
        result = 0
        for currUnique in range(1, maxUnique + 1):
            countMap = [0 for _ in range(26)]
            windowStart, windowEnd = 0, 0
            idx = 0
            unique = 0
            countAtLeastK = 0
            while windowEnd < len(s):
                # expand the sliding window
                if unique <= currUnique:
                    idx = ord(s[windowEnd]) - ord('a')
                    if countMap[idx] == 0:
                        unique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k:
                        countAtLeastK += 1
                    windowEnd += 1
                # shrink the sliding window
                else:
                    idx = ord(s[windowStart]) - ord('a')
                    if countMap[idx] == k:
                        countAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0:
                        unique -= 1
                    windowStart += 1

                if unique == currUnique and unique == countAtLeastK:
                    result = max(windowEnd - windowStart, result)
        return result

    # get the maximum number of unique letters in the string s
    def getMaxUniqueLetters(self, s: str):
        table = [False for _ in range(26)]
        maxUnique = 0
        for i in range(len(s)):
            if not table[ord(s[i]) - ord('a')]:
                maxUnique += 1
                table[ord(s[i]) - ord('a')] = True
        return maxUnique

    # 4th solution, simplified the 3rd solution, Sliding Window
    # O(n) time | O(1) space
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique = len(set(s))
        result = 0
        for currUnique in range(1, maxUnique + 1):
            countMap = {}
            windowStart, windowEnd = 0, 0
            unique = 0
            countAtLeastK = 0
            while windowEnd < len(s):
                # expand the sliding window
                if unique <= currUnique:
                    character = s[windowEnd]
                    if countMap.get(character, 0) == 0:
                        unique += 1
                    countMap[character] = countMap.get(character, 0) + 1
                    if countMap[character] == k:
                        countAtLeastK += 1
                    windowEnd += 1
                # shrink the sliding window
                else:
                    character = s[windowStart]
                    if countMap[character] == k:
                        countAtLeastK -= 1
                    countMap[character] -= 1
                    if countMap[character] == 0:
                        unique -= 1
                    windowStart += 1

                if unique == currUnique and unique == countAtLeastK:
                    result = max(windowEnd - windowStart, result)
        return result
