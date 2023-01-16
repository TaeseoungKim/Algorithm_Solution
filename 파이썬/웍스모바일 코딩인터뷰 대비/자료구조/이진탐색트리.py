class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, data):
        new_Node = Node(data)

        cur = self.root
        if cur == None:
            self.root = new_Node
            return
        while True:
            parent = cur
            if data < cur.data:
                cur = cur.left
                if not cur:
                    parent.left = new_Node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_Node
                    return
