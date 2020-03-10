import unittest
from node import NodeTree
from binary_tree_exception import NodeTypeError


class NodeTreeTest(unittest.TestCase):

    def test_getters_setters(self):
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

        # Test Exception
        self.assertRaises(NodeTypeError, lambda: node_root.setRight("1"))
        self.assertRaises(NodeTypeError, lambda: node_root.setLeft("2"))

    def test_kinship(self):
        node_root: NodeTree = NodeTree(7)
        node_left: NodeTree = NodeTree(5)
        node_right: NodeTree = NodeTree(9)

        node_root.setLeft(node_left)
        node_root.setRight(node_right)
        # Test is Brother
        self.assertFalse(node_root.isBrother(node_root))
        self.assertFalse(node_root.isBrother(node_right))
        self.assertFalse(node_root.isBrother(node_left))

        self.assertTrue(node_left.isBrother(node_right))
        self.assertFalse(node_left.isBrother(node_root))
        self.assertTrue(node_right.isBrother(node_left))
        self.assertFalse(node_right.isBrother(node_root))

        # test side
        self.assertFalse(node_root.isRight())
        self.assertFalse(node_root.isLeft())
        self.assertFalse(node_right.isLeft())
        self.assertTrue(node_right.isRight())
        self.assertTrue(node_left.isLeft())
        self.assertFalse(node_left.isRight())

        # Test is son
        self.assertTrue(node_left.isSon(node_root))
        self.assertTrue(node_right.isSon(node_root))
        self.assertFalse(node_root.isSon(node_right))
        self.assertFalse(node_root.isSon(node_left))

    def test_isLeaft_hasNode(self):
        node_a: NodeTree = NodeTree()
        node_b: NodeTree = NodeTree()
        node_c: NodeTree = NodeTree()
        node_d: NodeTree = NodeTree()
        node_e: NodeTree = NodeTree()

        node_a.setLeft(node_b)
        node_a.setRight(node_c)
        node_b.setLeft(node_d)
        node_c.setRight(node_e)
        """
                A
               /  \
              B    C
             /      \
            D        E    
        """

        # test isLeaf
        self.assertTrue(node_d.isLeaf())
        self.assertTrue(node_e.isLeaf())
        self.assertFalse(node_b.isLeaf())
        self.assertFalse(node_c.isLeaf())
        self.assertFalse(node_a.isLeaf())

        # test has node
        self.assertTrue(node_a.hasNodeLeft())
        self.assertTrue(node_a.hasNodeRight())

        self.assertTrue(node_b.hasNodeLeft())
        self.assertFalse(node_b.hasNodeRight())
        self.assertTrue(node_c.hasNodeRight())
        self.assertFalse(node_c.hasNodeLeft())

        self.assertFalse(node_d.hasNodeLeft())
        self.assertFalse(node_d.hasNodeRight())
        self.assertFalse(node_e.hasNodeLeft())
        self.assertFalse(node_e.hasNodeRight())


if __name__ == '__main__':
    unittest.main(exit=False)
