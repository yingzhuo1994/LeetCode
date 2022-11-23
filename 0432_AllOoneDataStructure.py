from collections import defaultdict
class AllOne:
    def __init__(self):
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {0: self.dll.get_sentinel()}

    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(pf)
        return

    def inc(self, key: str) -> None:
        pf = self.key_counter[key]
        self.key_counter[key] += 1
        cf = self.key_counter[key]
        if cf not in self.node_freq:
            # No need to test if pf = 0 since frequency zero points to sentinel node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key: str) -> None:
        if self.key_counter[key] > 0:
            pf = self.key_counter[key]
            self.key_counter[key] -= 1
            cf = self.key_counter[key]
            # if self.key_counter[key] == 0:
            #     self.key_counter.pop(key)
            if cf != 0:
                if cf not in self.node_freq:
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self) -> str:
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""
        
    def getMinKey(self) -> str:
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() > 0 else ""
            
class Node:
    def __init__(self):
        self.key_set = set([])
        self.prev, self.next = None, None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)    

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None
    
    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList:
    def __init__(self):
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        return

    def insert_after(self, node):
        newNode = Node()
        newNode.next = node.next
        newNode.prev = node
        node.next = newNode
        newNode.next.prev = newNode
        return newNode
    
    def insert_before(self, node):
        return self.insert_after(node.prev)

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        return

    def get_head(self):
        return self.sentinel.next
    
    def get_tail(self):
        return self.sentinel.prev

    def get_sentinel(self):
        return self.sentinel

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()