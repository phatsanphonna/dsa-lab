'''Lab 05 & 06'''


class BSTNode:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: BSTNode = None
        self.right: BSTNode = None


class BST:
    def __init__(self) -> None:
        self.root: BSTNode = None

    def isEmpty(self) -> bool:
        return self.root is None

    def preorder(self, root: BSTNode) -> None:
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root: BSTNode):
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root: BSTNode):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def insert(self, data: int) -> None:
        node = BSTNode(data)

        currentPointer: BSTNode = self.root

        if self.isEmpty():
            self.root = node
            return

        while currentPointer.left or currentPointer.right:
            print(currentPointer.data)

            if not currentPointer.left and data < currentPointer.data:
                currentPointer.left = node
                return
            elif not currentPointer.right and data >= currentPointer.data:
                currentPointer.right = node
                return

            if data < currentPointer.data:
                currentPointer = currentPointer.left
            else:
                currentPointer = currentPointer.right

        if data < currentPointer.data:
            currentPointer.left = node
        else:
            currentPointer.right = node

    def traverse(self) -> None:
        print('Preorder:', end=' ')
        self.preorder(self.root)
        print()

        print('Inorder:', end=' ')
        self.inorder(self.root)
        print()

        print('Postorder:', end=' ')
        self.postorder(self.root)
        print()


def main():
    tree = BST()
    tree.insert(14)
    tree.insert(23)
    tree.insert(7)
    tree.insert(10)
    tree.insert(15)
    tree.insert(33)
    tree.traverse()


if __name__ == '__main__':
    main()
