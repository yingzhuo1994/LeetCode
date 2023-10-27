class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        count = Counter(target)
        words = []
        wordSet = set()
        for sticker in stickers:
            c = Counter(sticker)
            dic = {}
            for ch in c:
                if ch not in count:
                    continue
                dic[ch] = c[ch]
            newWord = ""
            for ch in dic:
                newWord += ch * dic[ch]
            newWord = "".join(sorted(newWord))
            if len(newWord) > 0 and newWord not in wordSet:
                words.append(dic)
                wordSet.add(newWord)

        stack = deque([["".join(sorted(target)), 1]])
        visited = set()
        while stack:
            t, ans = stack.popleft()
            count = Counter(t)
            for word in words:
                new = count.copy()
                for ch in word:
                    new[ch] = max(0, count[ch] - word[ch])
                newWord = ""
                for ch in new:
                    newWord += ch * new[ch]
                newWord = "".join(sorted(newWord))
                if newWord == "":
                    return ans
                elif newWord not in visited:
                    stack.append([newWord, ans + 1])
                    visited.add(newWord)
        return -1