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
        return not self.root

    def printPreOrder(self, root: BSTNode) -> None:
        if (root != None):
            print("->", root.data, end=" ")
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    def printInOrder(self, root: BSTNode) -> None:
        if (root != None):
            self.printInOrder(root.left)
            print("->", root.data, end=" ")
            self.printInOrder(root.right)

    def printPostOrder(self, root: BSTNode) -> None:
        if (root != None):
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print("->", root.data, end=" ")

    def insert(self, data: int) -> None:
        currentPointer: BSTNode = self.root

        if self.isEmpty():
            self.root = BSTNode(data)
            return

        while currentPointer.left or currentPointer.right:
            if not currentPointer.left and data < currentPointer.data:
                currentPointer.left = BSTNode(data)
                return
            elif not currentPointer.right and data >= currentPointer.data:
                currentPointer.right = BSTNode(data)
                return

            if data < currentPointer.data:
                currentPointer = currentPointer.left
            else:
                currentPointer = currentPointer.right

        if data < currentPointer.data:
            currentPointer.left = BSTNode(data)
        else:
            currentPointer.right = BSTNode(data)

    # def delete(self, data: int) -> int:
    #     node: BSTNode = BSTNode(data)

    #     previousPointer: BSTNode = None
    #     currentPointer: BSTNode = self.root
    #     found: BSTNode = None

    #     while currentPointer.left or currentPointer.right:
    #         if currentPointer.data == node.data and not found:
    #             found = currentPointer
    #             continue

    #         if data < currentPointer.data:
    #             previousPointer = currentPointer

    #             if not currentPointer.left:
    #                 currentPointer = currentPointer.right
    #             else:
    #                 currentPointer = currentPointer.left
    #         else:
    #             previousPointer = currentPointer

    #             if not currentPointer.right:
    #                 currentPointer = currentPointer.left
    #             else:
    #                 currentPointer = currentPointer.right

    #     if not found:
    #         return None

    #     finalPointer: BSTNode = None

    #     if previousPointer.data > currentPointer.data:
    #         finalPointer = previousPointer
    #     else:
    #         finalPointer = currentPointer

    #     print('foundPointer:', found.data)
    #     print('finalPointer:', finalPointer.data)
    #     print('previousPointer:', previousPointer.data)
    #     print('currentPointer:', currentPointer.data)

    #     if previousPointer.left == finalPointer:
    #         previousPointer.left = None
    #     elif previousPointer.right == finalPointer:
    #         previousPointer.right = None

    #     previousPointer.left = self.root.left
    #     previousPointer.right = currentPointer
    #     self.root = previousPointer

    # def delete(self, data: int) -> None:
    #     if self.isEmpty():
    #         return None

    #     currentPointer: BSTNode = self.root
    #     previousPointer: BSTNode = None
    #     found: BSTNode = None

    #     # Find the node to be deleted
    #     while currentPointer:
    #         if currentPointer.data == data:
    #             found = currentPointer
    #             break

    #         previousPointer = currentPointer
    #         if data < currentPointer.data:
    #             currentPointer = currentPointer.left
    #         else:
    #             currentPointer = currentPointer.right

    #     # Node not found
    #     if not found:
    #         return

    #     # Node to be deleted has no children
    #     if not found.left and not found.right:
    #         if not previousPointer:
    #             self.root = None
    #         elif previousPointer.left == found:
    #             previousPointer.left = None
    #         else:
    #             previousPointer.right = None
    #         return

    #     # Node to be deleted has only one child
    #     if not found.left or not found.right:
    #         child = found.left or found.right

    #         if not previousPointer:
    #             self.root = child
    #         elif previousPointer.left == found:
    #             previousPointer.left = child
    #         else:
    #             previousPointer.right = child
    #         return

    #     # Node to be deleted has two children
    #     replaceNode = found.right
    #     beforeReplaceNode = found

    #     while replaceNode.left:
    #         beforeReplaceNode = replaceNode
    #         replaceNode = replaceNode.left

    #     found.data = replaceNode.data

    #     if beforeReplaceNode.left == replaceNode:
    #         beforeReplaceNode.left = replaceNode.right
    #     else:
    #         beforeReplaceNode.right = replaceNode.right

    def delete(self, data: int):
        def findMax(tree: BSTNode):
            if tree.right is None:
                return tree.data
            return findMax(tree.right)

        def runDelete(tree: BSTNode, data: int):
            if tree is None:
                print("%d not found in your Binary Tree" % data)
                return

            if data > tree.data:
                tree.right = runDelete(tree.right, data)
            elif data < tree.data:
                tree.left = runDelete(tree.left, data)
            else:
                if tree.left is None and tree.right is None:
                    tree = None
                elif tree.left is None and tree.right.left is None:
                    tree = tree.right
                elif tree.right is None and tree.left.right is None:
                    tree = tree.left
                else:
                    leftLargestNode = findMax(tree.left)
                    tree.data = leftLargestNode
                    tree.left = runDelete(tree.left, leftLargestNode)

            return tree

        self.root = runDelete(self.root, data)

    def findMin(self) -> int:
        if self.isEmpty():
            return None

        minValue = float('inf')

        def preorder(root: BSTNode) -> None:
            nonlocal minValue

            if root != None:
                if root.data < minValue:
                    minValue = root.data

                preorder(root.left)
                preorder(root.right)

        preorder(self.root)

        return minValue

    def findMax(self) -> int:
        if self.isEmpty():
            return None

        maxValue = float('-inf')

        def preorder(root: BSTNode) -> None:
            nonlocal maxValue

            if root != None:
                if root.data > maxValue:
                    maxValue = root.data

                preorder(root.left)
                preorder(root.right)

        preorder(self.root)

        return maxValue

    def traverse(self) -> None:
        print('Preorder:', end=' ')
        self.printPreOrder(self.root)
        print()

        print('Inorder:', end=' ')
        self.printInOrder(self.root)
        print()

        print('Postorder:', end=' ')
        self.printPostOrder(self.root)
        print()


def main():
    tree = BST()
    tree.insert(14)
    tree.insert(23)
    tree.insert(7)
    tree.insert(10)
    tree.insert(33)
    tree.traverse()
    print()
    tree.delete(14)
    tree.traverse()
    print("Min:", tree.findMin())
    print("Max:", tree.findMax())


if __name__ == '__main__':
    main()
