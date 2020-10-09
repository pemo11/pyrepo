# Aus Data Structures and Algorithm-Buch

class BinarySearchTree:

    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self, newval):
            self.val = newval

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newval):
            self.left = newval

        def setRight(self, newval):
            self.right = newval

        def __iter__(self):
            if self.left != None:
                for el in self.left:
                    yield el

            yield self.val

            if self.right != None:
                for el in self.right:
                    yield el
                    
    def __init__(self):
        self.root = None

    def insert(self, val):

        def __insert(root, val):
            if root == None:
                return BinarySearchTree.__Node(val)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(), val))
            else:
                root.setRight(__insert(root.getRight(), val))
            return root
    
        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

def main():
    s = input("Gib eine Liste von Zahlen ein:")
    zahlen = s.split()

    tree = BinarySearchTree()

    for z in zahlen:
        tree.insert(float(z))

    for z in tree:
        print(z)

if __name__ == "__main__":
    main()

