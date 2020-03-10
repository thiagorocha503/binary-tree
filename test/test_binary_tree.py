import unittest
from node import NodeTree
from binary_tree import BinaryTree


class BinaryTreeTest(unittest.TestCase):

    def test_add_find(self):
        tree: BinaryTree = BinaryTree()
        root: NodeTree = tree.getRoot()
        """
              *
        """
        self.assertIsInstance(tree, BinaryTree)
        self.assertEqual(tree.find(3), None)
        self.assertEqual(root.getInfo(), None)
        self.assertEqual(root.getRight(), None)
        self.assertEqual(root.getLeft(), None)

        """
                  7
                  |
            5 -----------9

        """
        tree.add(7)
        tree.add(5)
        tree.add(9)
        # Teste find
        self.assertEqual(tree.find(7), root)
        self.assertEqual(tree.find(5), root.getLeft())
        self.assertEqual(tree.find(9), root.getRight())

        # Teste valor do nó
        self.assertEqual(root.getInfo(), 7)
        self.assertEqual(root.getLeft().getInfo(), 5)
        self.assertEqual(root.getRight().getInfo(), 9)

        """
                  7
                  |
            5 -----------9
            |            |
        3 ---- 6      8 ---- 10

        """
        tree.add(3)
        tree.add(6)
        tree.add(8)
        tree.add(10)
        # Test find
        self.assertEqual(tree.find(3), root.getLeft().getLeft())
        self.assertEqual(tree.find(6), root.getLeft().getRight())
        self.assertEqual(tree.find(10), root.getRight().getRight())
        self.assertEqual(tree.find(8), root.getRight().getLeft())

        # teste valor do nó
        self.assertEqual(root.getLeft().getLeft().getInfo(), 3)
        self.assertEqual(root.getLeft().getRight().getInfo(), 6)
        self.assertEqual(root.getRight().getRight().getInfo(), 10)
        self.assertEqual(root.getRight().getLeft().getInfo(), 8)

    def test_remove(self):
        tree: BinaryTree = BinaryTree()
        root: NodeTree = tree.getRoot()
        for number in [7, 5, 9, 3, 6, 8, 10]:
            tree.add(number)

        """
                  7
                  |
            5 -----------9
            |            |
        3 ---- 6      8 ---- 10


        """
        # verifica valores
        self.assertEqual(root.getInfo(), 7)
        self.assertEqual(root.getLeft().getInfo(), 5)
        self.assertEqual(root.getRight().getInfo(), 9)
        self.assertEqual(root.getLeft().getLeft().getInfo(), 3)
        self.assertEqual(root.getLeft().getRight().getInfo(), 6)
        self.assertEqual(root.getRight().getRight().getInfo(), 10)
        self.assertEqual(root.getRight().getLeft().getInfo(), 8)
        #
        # Test remove node leaf
        #
        """
                  7
                  |
            5 -----------9
            |            |
         3 ---           --- 10
        """
        # folha esquerda e direita
        tree.remove(6)
        self.assertIsNone(tree.find(6))
        self.assertIsInstance(root.getLeft().getLeft(), NodeTree)
        self.assertEqual(root.getLeft().getRight(), None)

        tree.remove(8)
        self.assertIsNone(tree.find(8))
        self.assertIsInstance(root.getRight().getRight(), NodeTree)
        self.assertIsNone(root.getRight().getLeft(), None)

        #
        #   Test remove node with one node
        #
        """
                  7                     7
                  |                     |
            5 ----------- 9  ->    3 ------- 10
            |             |
        3 ---             ---10
        
        """
        # Nó com subárvore esquerda
        tree.remove(5)
        self.assertIsNone(tree.find(5))
        self.assertEqual(root.getLeft().getInfo(), 3)
        self.assertIsNone(root.getLeft().getLeft())
        self.assertIsNone(root.getLeft().getRight())

        # Nó com subárvore direita
        tree.remove(9)
        self.assertIsNone(tree.find(9))
        self.assertEqual(root.getRight().getInfo(), 10)
        self.assertIsNone(root.getRight().getRight())
        self.assertIsNone(root.getRight().getLeft())


if __name__ == '__main__':
    unittest.main(exit=False)
