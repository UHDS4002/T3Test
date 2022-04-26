import os.path
from typing import Optional
from unittest import TestCase, main


class Node:
    def __init__(self, data):
        self.data = data
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None


class TestIsBST(TestCase):
    def test_api(self):
        import is_bst
        self.assertTrue(os.path.exists('is_bst.py'),
                        "is_bst.py does not exist.")
        self.assertTrue(hasattr(is_bst, "is_bst"),
                        "is_bst function is not defined")

    def test_simple(self):
        from is_bst import is_bst
        root = Node(10)
        self.assertTrue(is_bst(root))
        root.left = Node(5)
        self.assertTrue(is_bst(root))
        root.right = Node(11)
        self.assertTrue(is_bst(root))
        root.right.right = Node(15)
        self.assertTrue(is_bst(root))
        root.right.right.left = Node(17)
        self.assertFalse(is_bst(root))

    def test_complex(self):
        from is_bst import is_bst
        root = Node(10)
        root.left = Node(7)
        root.left.right = Node(11)
        self.assertFalse(is_bst(root),
                         "This Is Not BST!")


if __name__ == '__main__':
    main()
