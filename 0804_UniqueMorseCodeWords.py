# 1st solution
# O(n) time | O(n) space
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniqueSet = set()
        for word in words:
            stack = []
            for ch in word:
                idx = ord(ch) - ord('a')
                stack.append(Morse[idx])
            code = "".join(stack)
            uniqueSet.add(code)
        return len(uniqueSet)