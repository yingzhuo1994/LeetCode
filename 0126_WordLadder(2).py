# 1st solution
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
    
        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]] # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = collections.defaultdict(list) # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord: 
                    return layer[word] # return all found sequences
                for i in range(len(word)): # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer

        return []

# 2nd solution
# O(n*26^l) time | O(n + k * p) space
# where n is the length of wordList, l is the longest length of words
# k is number of paths, p is path length.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
    
        wordSet = set(wordList) 
        layer = {}
        layer[beginWord] = [[beginWord]] 
        alpha = string.ascii_lowercase 

        while layer:
            newlayer = collections.defaultdict(list) 
            for word in layer:
                if word == endWord: 
                    return layer[word] 
                for i in range(len(word)): 
                    for c in alpha:
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [lst + [newWord] for lst in layer[word]] 
            wordSet -= set(newlayer.keys())
            layer = newlayer 

        return []