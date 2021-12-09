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

# 2nd solution, Bitmask
# O(n*N + m*2^M) time | O(n) space
# where n, m are the length of words and puzzles, respectively,
# and n, m are the average length of words[i] and puzzles[i] respectively.
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        def bitmask(word: str) -> int:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            return mask

        # Create a bitmask for each word.
        word_count = Counter(bitmask(word) for word in words)

        result = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            count = word_count[first]

            # Make bitmask but ignore the first character since it must always
            # be there.
            mask = bitmask(puzzle[1:])

            # Iterate over every possible subset of characters.
            submask = mask
            while submask:
                # Increment the count by the number of words that match the
                # current submask.
                count += word_count[submask | first]  # add first character
                submask = (submask - 1) & mask
            result.append(count)
        return result