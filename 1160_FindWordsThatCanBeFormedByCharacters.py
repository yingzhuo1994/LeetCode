class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        ans = 0
        for word in words:
            dic = Counter(word)
            if all(dic[ch] <= count[ch] for ch in dic):
                ans += len(word)
        return ans