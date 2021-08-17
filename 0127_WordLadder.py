class Solution:
    # 1st solution
    # O(n*26^k) time | O(n) space
    # where k is the length of beginword, and n is the length of wordList
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        arr = set(wordList) #avoid TLE
        q = collections.deque([(beginWord, 1)])
        visted = set()
        alpha = string.ascii_lowercase  #'abcd...z'
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in arr and new_word not in visted:
                        q.append((new_word, length + 1))
                        visted.add(new_word)
        return 0

    # 2nd solution
    # O(n*26^k) time | O(n) space
    # where k is the length of beginword, and n is the length of wordList
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList) #avoid TLE
        q = collections.deque([(beginWord, 1)])
        alpha = string.ascii_lowercase  #'abcd...z'
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in  word_set:
                        q.append((new_word, length + 1))
                        word_set.remove(new_word)
        return 0