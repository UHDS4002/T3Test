import os.path
from typing import Optional
from unittest import TestCase, main


class Node:
    def __init__(self, data):
        self.data = data
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None


class TestFixer(TestCase):
    def test_api(self):
        self.assertTrue(os.path.exists("fix_bst.py"),
                        "Module fix_bst.py does not exist")
        import fix_bst
        self.assertTrue(hasattr(fix_bst, 'fix_bst'),
                        'function fix_bst is not defined.')
        self.assertTrue(hasattr(fix_bst.fix_bst, '__call__'),
                        'fix_bst is not function (or callable)')

    def test_simple(self):
        from fix_bst import fix_bst
        root = Node(10)
        root.left = Node(15)
        fix_bst(root)
        self.assertIsNone(root.left,
                          "root's left child was the bad node, you should of removed it.")

        l1 = root.left = Node(8)
        l2 = root.left.right = Node(9)
        l3 = root.right = Node(15)
        root.right.left = Node(16)
        fix_bst(root)
        self.assertIs(l1, root.left, "Why root.left is missing?")
        self.assertIs(l2, root.left.right, "Why root.left.right is missing?")
        self.assertIs(l3, root.right, "Why root.right is missing?")
        self.assertIsNone(root.right.left, "Whe root.right.left is not removed?")


if __name__ == '__main__':
    main()
