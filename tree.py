class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Binary_tree:
    def __init__(self, data):
        node = Node(data)
        self.root = node

    #in order/symmetrical
    def symmetrical_order(self, node=None):
        if node is None:
            node = self.root
        #starting from the left
        if node.left:
            print('(', end='')
            self.symmetrical_order(node.left)
        print(node, end='')
        if node.right:
            print(')', end='')
            self.symmetrical_order(node.right)

    #post_order
    def post_order(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node, end='')

    def pre_order(self, node=None):
        if node is None:
            node = self.root
        print(node, end='')
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)
        

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = hright = 0
        if node.left:
            self.height(node.left)
        if node.right:
            self.height(node.right)
        if hleft > hright:
            return hleft+1
        return hright+1

    