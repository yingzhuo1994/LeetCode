class Solution:
    # 1st solution
    def letterCasePermutation(self, s: str) -> List[str]:
        index = []
        for i, ch in enumerate(s):
            if ch.isalpha():
                index.append(i)
        if len(index) == 0:
            return [s]
        result = []
        for i in index:
            large = s[i].upper()
            small = s[i].lower()
            if len(result) == 0:
                result.append(s[:i] + large + s[i + 1:])
                result.append(s[:i] + small + s[i + 1:])
            else:
                new = []
                new.extend([lst[:i] + large + lst[i + 1:] for lst in result])
                new.extend([lst[:i] + small + lst[i + 1:] for lst in result])
                result = new
        return result