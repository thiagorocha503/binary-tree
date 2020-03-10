from binary_tree_exception import NodeTypeError


class NodeTree:

    def __init__(self, inf=None):
        self.__info = inf
        self.__left: NodeTree or None = None
        self.__right: NodeTree or None = None
        self.__father: NodeTree or None = None

    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info = info

    def getFather(self):
        return self.__father

    def __setFather(self, father):
        if isinstance(father, NodeTree) or father is None:
            self.__father = father
        else:
            raise NodeTypeError(father)

    def getRight(self):
        return self.__right

    def setRight(self, node):
        if not isinstance(node, NodeTree) and node is not None:
            raise NodeTypeError(node)
        self.__right = node
        if node is not None:
            self.__right.__setFather(self)

    def getLeft(self):
        return self.__left

    def setLeft(self, node):
        if not isinstance(node, NodeTree) and node is not None:
            raise NodeTypeError(node)
        self.__left = node
        if node is not None:
            self.__left.__setFather(self)

    def isSon(self, node) -> bool:
        if not isinstance(node, NodeTree):
            raise NodeTypeError(node)
        if node is not None:
            if self.__father == node:
                return True
            else:
                return False
        else:
            return False

    def isBrother(self, node) -> bool:
        if not isinstance(node, NodeTree):
            raise NodeTypeError(node)
        if node is not None:
            if node.getFather() == self.__father and (node.getFather() is not None and self.__father is not None):
                return True
            else:
                return False
        else:
            return False

    def isLeft(self) -> bool:
        if self.__father is None:
            return False
        else:
            if self.__father.getLeft() == self:
                return True
            else:
                return False

    def isRight(self) -> bool:
        if self.__father is None:
            return False
        else:
            if self.__father.getRight() == self:
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
