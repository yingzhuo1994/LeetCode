# 1st solution
# O(mn*3^T) time | O(k) space
# where m and n are sizes of our board and T is the length fo the longest word in words
# k is sum of length of all words.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # to prvent TLE
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words: trie.insert(word) 

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0: return

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return 
        tmp = board[i][j]
        if tmp not in node.children: return

        board[i][j] = "#"
        for x,y in [[0,-1], [0,1], [1,0], [-1,0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
        board[i][j] = tmp

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1

# 2nd solution
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        root = Node()
        for word in words:
            cur = root 
            for ch in word:
                cur = cur.children[ch]
            cur.isEnd = True 
        
        res = []
        
        dirs = [(1, 0), (-1, 0), (0, 1),(0,-1)]
        def dfs(i, j, node): 
            if node.isEnd: 
                res.append(''.join(word))
                node.isEnd = False 
            if i >= row or i < 0 or j >= col or j < 0: return 
            if not board[i][j]: return
            if board[i][j] in node.children:
                temp = board[i][j]
                board[i][j] = None
                word.append(temp)
                cur_node = node.children[temp] 
                for dx, dy in dirs:
                    dfs(i + dx, j + dy, cur_node)
                board[i][j] = temp 
                if not cur_node.children: del node.children[temp]
                word.pop()         
            
        for i in range(row):
            for j in range(col):
                cur = root
                word = []
                dfs(i, j, cur)
        return res 

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isEnd = False

# 3rd solution
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        frags = set()
        for i in range(m):
            for j in range(n):
                frags.add(board[i][j])
                if i:
                    frags.add(board[i-1][j] + board[i][j])
                    frags.add(board[i][j] + board[i-1][j])
                if j:
                    frags.add(board[i][j-1] + board[i][j])
                    frags.add(board[i][j] + board[i][j-1])
        
        allwords = Trie()
        for w in words:
            prev = ''
            for ch in w:
                if ch not in frags or prev+ch not in frags:
                    break
                prev = ch
            else:
                allwords.add(w)
            
        found = []
        def do_search(x, y, t, s):
            curCh = board[x][y]
            board[x][y] = "#"
            if t.final:
                found.append(s)
                allwords.remove(s)
            for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != "#":
                    ch = board[nx][ny]
                    nt = t[ch]
                    if nt is not None:
                        do_search(nx, ny, nt, s + ch)
            board[x][y] = curCh
        
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                t = allwords[ch]
                if t is not None:
                    do_search(i, j, t, ch)
        return found

class Trie:
    def __init__(self):
        self.nxt = defaultdict(Trie)
        self.final = False
    
    def __getitem__(self, ch):
        return self.nxt.get(ch, None)
    
    def __repr__(self):
        return f"Trie[{'final, ' if self.final else ''}'{''.join(self.nxt.keys())}']"

        
    def add(self, s):
        if s == "":
            self.final = True
        else:
            self.nxt[s[0]].add(s[1:])
            
    def remove(self, s):
        if s == "":
            self.final = False
        else:
            ch = s[0]
            if ch in self.nxt:
                self.nxt[ch].remove(s[1:])
                if not self.nxt[ch].nxt and not self.nxt[ch].final:
                    del self.nxt[ch]