from node import NodeTree
from binary_tree_exception import NodeTypeError


class BinaryTree:

    def __init__(self):
        self.__root: NodeTree = NodeTree()

    def getRoot(self) -> NodeTree:
        return self.__root

    def remove(self, value):
        if self.__root is None:
            return
        if self.__root.getInfo() is None:
            return
        self.__remove(self.__root, value)

    def __remove(self, node: NodeTree, value):
        # case found
        if node.getInfo() == value:
            parent: NodeTree = node.getParent()
            if node.getParent() is None:
                raise Exception("Remoção de nó raiz")
            if (node.getLeft() is None) and (node.getRight() is None):
                # print("Nó folha")
                if node.isLeft():
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
            elif (node.getLeft() is not None) and (node.getRight() is None):
                # print("Subárvore esquerda")
                if node.isLeft():
                    parent.setLeft(node.getLeft())
                else:
                    parent.setRight(node.getRight())
            elif (node.getLeft() is None) and (node.getRight() is not None):
                if node.isLeft():
                    parent.setLeft(node.getRight())
                else:
                    parent.setRight(node.getRight())

                # print("Subárvore direita")
            else:
                raise Exception("Nó com subárvore esquerda e direita")

        else:
            if value < node.getInfo():
                self.__remove(node.getLeft(), value)
            else:
                self.__remove(node.getRight(), value)

    def add(self, value):
        if self.__root is None:
            self.__root = NodeTree(value)
            return
        self.__add(self.__root, value)

    def __add(self, node_: NodeTree, value):
        # inf
        if node_.getInfo() is None:
            node_.setInfo(value)
        else:
            # left
            if value < node_.getInfo():
                if node_.getLeft() is None:
                    node_.setLeft(NodeTree(value))
                else:
                    self.__add(node_.getLeft(), value)
            else:  # right
                if node_.getRight() is None:
                    node_.setRight(NodeTree(value))
                else:
                    self.__add(node_.getRight(), value)

    def hasValue(self, value) -> bool:
        if self.find(value) is None:
            return False
        else:
            return True

    def find(self, value) -> NodeTree or None:
        if self.__root is None:
            return None
        if self.__root.getInfo() is None:
            return None
        return self.__find(self.__root, value)

    def __find(self, node_: NodeTree, value) -> NodeTree or None:
        if node_ is None:
            return None
        if not isinstance(node_, NodeTree):
            raise NodeTypeError(node_)
        if node_.getInfo() == value:
            return node_
        else:
            if value < node_.getInfo():  # node left
                if node_.getLeft() is not None:
                    return self.__find(node_.getLeft(), value)
                else:
                    return None
            else:  # node right
                if node_.getRight() is not None:
                    return self.__find(node_.getRight(), value)
                else:
                    return None

    def clear(self) -> None:
        self.__root = None
