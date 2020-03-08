from node import NodeTree
import unittest


class NodeTreeTest(unittest.TestCase):

    def test(self):
        node_root: NodeTree = NodeTree()
        # inicialização
        self.assertEqual(node_root.getInfo(), None)
        self.assertEqual(node_root.getLeft(), None)
        self.assertEqual(node_root.getRight(), None)
        self.assertEqual(node_root.getFather(), None)

        root_value = 7
        node_left_value = 5
        node_right_value = 9

        # getters e setters
        node_root.setInfo(root_value)
        node_left: NodeTree = NodeTree(node_left_value)
        node_right: NodeTree = NodeTree(node_right_value)
        node_root.setLeft(node_left)
        node_root.setRight(node_right)

        self.assertEqual(node_root.getInfo(), root_value)
        self.assertEqual(node_root.getLeft(), node_left)
        self.assertEqual(node_root.getLeft().getInfo(), node_left_value)
        self.assertEqual(node_root.getLeft().getFather(), node_root)

        self.assertEqual(node_root.getRight(), node_right)
        self.assertEqual(node_root.getRight().getInfo(), node_right_value)
        self.assertEqual(node_root.getRight().getFather(), node_root)


if __name__ == '__main__':
    unittest.main()
