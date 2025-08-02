class TextEditor:

    def __init__(self):
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start
        self.end.next = self.start
        self.start.prev = self.end
        self.cur = self.start
        self.pos = 0

    def addText(self, text: str) -> None:
        if self.pos == self.cur.size():
            node = Node(text)
            self.cur.append(node)
            self.cur = node
            self.pos = len(text) 
        else:
            self.cur.text = self.cur.text[:self.pos] + text + self.cur.text[self.pos:]
            self.pos += len(text)
            if self.cur.size() > 40:
                front = self.cur.text[:40]
                back = self.cur.text[40:]
                self.cur.text = front
                node = Node(back)
                self.cur.append(node)
                if self.pos > self.cur.size():
                    self.pos -= self.cur.size()
                    self.cur = self.cur.next
        # self.printText()

    def deleteText(self, k: int) -> int:
        if self.cur == self.start:
            return 0
        if self.pos <= k:
            node = self.cur
            m = self.pos
            node.text = node.text[self.pos:]
            if node.size == self.pos:
                nextNode = node.next
                nextNode.prev = node.prev
                node.prev.next = nextNode
            k -= self.pos
            self.cur = node.prev           
            self.pos = self.cur.size()
            return m + self.deleteText(k)
        else:
            self.cur.text = self.cur.text[:self.pos-k] + self.cur.text[self.pos:]
            self.pos -= k
        # self.printText()
        return k
            

    def cursorLeft(self, k: int) -> str:
        # print(k, self.cur.text, self.pos, "/", len(self.cur.text))
        if k < self.pos:
            self.pos -= k
        else:
            if self.cur != self.start:
                self.cur = self.cur.prev
                k -= self.pos
                self.pos = self.cur.size()
                return self.cursorLeft(k)
            else:
                self.cur = self.start
                self.pos = 0
        # print(self.pos)
        # self.printText()
        return self.getLeftStr() 


    def cursorRight(self, k: int) -> str:
        if k + self.pos <= self.cur.size():
            self.pos += k
        else:
            if self.cur.next != self.end:
                k = k + self.pos - self.cur.size()
                self.cur = self.cur.next
                self.pos = 0
                # print("test", k)
                return self.cursorRight(k)
            else:
                self.pos = self.cur.size()
        # self.printText()
        return self.getLeftStr()     

    def getLeftStr(self):
        node = self.cur
        pos = self.pos
        text = ""
        while node is not self.start and len(text) < 10:
            text = node.text[:pos] + text
            node = node.prev
            pos = node.size()
        if len(text) >= 10:
            return text[-10:]
        return text

    def printText(self):
        node = self.start
        text = ""
        while node is not self.end:
            if node == self.cur:
                text += node.text[:self.pos] + "|" + node.text[self.pos:]
            else:
                text += node.text
            node = node.next
        print(text, self.pos, "/", self.cur.size(), self.cur.text)
                

class Node:
    def __init__(self, text=""):
        self.text = text
        self.prev = None
        self.next = None
    
    def size(self):
        return len(self.text)
    
    def append(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)