from binary_tree_exception import NodeTypeError


class NodeTree:

    def __init__(self, inf=None):
        self.__info = inf
        self.__left: NodeTree or None = None
        self.__right: NodeTree or None = None
        self.__parent: NodeTree or None = None

    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info = info

    def getParent(self):
        return self.__parent

    def __setParent(self, father):
        if isinstance(father, NodeTree) or father is None:
            self.__parent = father
        else:
            raise NodeTypeError(father)

    def getRight(self):
        return self.__right

    def setRight(self, node):
        if not isinstance(node, NodeTree) and node is not None:
            raise NodeTypeError(node)
        self.__right = node
        if node is not None:
            self.__right.__setParent(self)

    def getLeft(self):
        return self.__left

    def setLeft(self, node):
        if not isinstance(node, NodeTree) and node is not None:
            raise NodeTypeError(node)
        self.__left = node
        if node is not None:
            self.__left.__setParent(self)

    def isSon(self, node) -> bool:
        if not isinstance(node, NodeTree):
            raise NodeTypeError(node)
        if node is not None:
            if self.__parent == node:
                return True
            else:
                return False
        else:
            return False

    def isBrother(self, node) -> bool:
        if not isinstance(node, NodeTree):
            raise NodeTypeError(node)
        if node is not None:
            if node.getParent() == self.__parent and (node.getParent() is not None and self.__parent is not None):
                return True
            else:
                return False
        else:
            return False

    def isLeft(self) -> bool:
        if self.__parent is None:
            return False
        else:
            if self.__parent.getLeft() == self:
                return True
            else:
                return False

    def isRight(self) -> bool:
        if self.__parent is None:
            return False
        else:
            if self.__parent.getRight() == self:
                return True
            else:
                return False

    def isLeaf(self) -> bool:
        if self.__left is None and self.__right is None:
            return True
        else:
            return False

    def hasNodeLeft(self) -> bool:
        if isinstance(self.__left, NodeTree):
            return True
        else:
            return False

    def hasNodeRight(self):
        if isinstance(self.__right, NodeTree):
            return True
        else:
            return False
