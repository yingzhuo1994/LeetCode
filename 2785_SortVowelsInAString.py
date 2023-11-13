# 1st solution
# O(n) time | O(n) space
class Solution:
    def sortVowels(self, s: str) -> str:
        count = Counter(s)
        stack = []
        vowels = list("aeiouAEIOU")
        vowels.sort()
        idx = 0
        for ch in s:
            if ch in vowels:
                while True:
                    while vowels[idx] not in count:
                        idx += 1
                    vowel = vowels[idx]
                    if count[vowel] == 0:
                        idx += 1
                    else:
                        stack.append(vowel)
                        count[vowel] -= 1
                        break
            else:
                stack.append(ch)
        return "".join(stack)

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:    
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels, positions = [], [] 
        vowelSet = set(list("aeiouAEIOU"))
    
        for i, c in enumerate(s):
            if c in vowelSet:
                vowels.append(c)
                positions.append(i)
        
        vowels.sort()

        for i, c in zip(positions, vowels):
            s[i] = c
        
        return ''.join(s)