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
        wordSet = set(wordList)
        if endWord not in wordSet:
            return [] 
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

# 3rd solution, bi-direction
# O(n*26^l) time | O(n + k * p) space
# where n is the length of wordList, l is the longest length of words
# k is number of paths, p is path length.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord or not beginWord or not wordList or endWord not in wordList \
            or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Build graph, bi-BFS
        # ans = []
        bqueue = collections.deque()
        bqueue.append(beginWord)
        equeue = collections.deque()
        equeue.append(endWord)
        bvisited = set([beginWord])
        evisited = set([endWord])
        rev = False 
        #graph
        parents = collections.defaultdict(set)
        found = False 
        depth = 0
        while bqueue and not found:
            depth += 1 
            length = len(bqueue)
            # print(queue)
            localVisited = set()
            for _ in range(length):
                word = bqueue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == word:
                            continue
                        if nextWord not in bvisited:
                            if not rev:
                                parents[nextWord].add(word)
                            else:
                                parents[word].add(nextWord)
                            if nextWord in evisited:    
                                found = True
                            localVisited.add(nextWord)
                            bqueue.append(nextWord)
            bvisited = bvisited.union(localVisited)
            bqueue, bvisited, equeue, evisited, rev = equeue, evisited, bqueue, bvisited, not rev
        # print(parents)
        # print(depth)
        # Search path, DFS
        ans = []
        def dfs(node, path, d):
            if d == 0:
                if path[-1] == beginWord:
                    ans.append(path[::-1])
                return 
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, d-1)
                path.pop()
        dfs(endWord, [endWord], depth)
        return ans