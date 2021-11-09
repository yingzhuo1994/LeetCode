# 1st solution, TLE
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordsList = [set(word) for word in words]
        puzzlesList = [set(puzzle) for puzzle in puzzles]
        result = [0 for _ in puzzles]
        for i, puzzle in enumerate(puzzles):
            for j, word in enumerate(words):
                if self.checkFirstLetter(puzzle[0], wordsList[j]) and self.checkEachLetter(puzzlesList[i], wordsList[j]):
                    result[i] += 1
        return result    

    def checkFirstLetter(self, firstLetter, wordSet):
        if firstLetter in wordSet:
            return True
        return False
    
    def checkEachLetter(self, puzzleSet, wordSet):
        for letter in wordSet:
            if letter not in puzzleSet:
                return False
        return True
