# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        p = self
        while p:
            if value < p.value:
                if p.left is None:
                    p.left = BST(value)
                    break
                p = p.left
            else:
                if p.right is None:
                    p.right = BST(value)
                    break
                p = p.right
        return self

    def contains(self, value):
        # Write your code here.
        p = self
        while p is not None:
            if value < p.value:
                p = p.left
            elif value > p.value:
                p = p.right
            else:
                return True
        return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        parentNode = None
        currentNode = self
        if self.contains(value):
            # print('test contains')
            while currentNode:
                if value > currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.right
                elif value < currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.left
                else:
                    if parentNode == None and currentNode.left is None and currentNode.right is None:
                        break
                    if currentNode.left is None and currentNode.right is None:
                        if parentNode.left == currentNode:
                            parentNode.left = None
                        else:
                            parentNode.right = None
                    elif currentNode.left is not None and currentNode.right is None:
                        if parentNode.left == currentNode:
                            parentNode.left = currentNode.left
                        else:
                            parentNode.right = currentNode.left
                    elif currentNode.left is None and currentNode.right is not None:
                        if parentNode.left == currentNode:
                            parentNode.left = currentNode.right
                        else:
                            parentNode.right = currentNode.right
                    else:
                        # print('find the place')
                        currentNode.value = currentNode.right.findSmallest()
                    break
        return self

    def findSmallest(self):
        p = self
        parentNode = None
        while p.left:
            parentNode = p
            p = p.left
        value = p.value
        if p.right is None:
            parentNode.left = None
        else:
            parentNode.left = p.right
        return value

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.value) + "\n"
            if t.right:
                tree_str += print_tree(t.right, indent + 1)
            if t.left:
                tree_str += print_tree(t.left, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

# print(root)
root.insert(12)
print(root)
# print(root.right.left.left.value == 12)
#
root.remove(10)
# print(root)

# self.assertTrue(not root.contains(10))
# self.assertTrue(root.value == 12)
#
# self.assertTrue(root.contains(15))
