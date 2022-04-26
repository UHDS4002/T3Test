import os.path
from unittest import TestCase, main


class TestFind(TestCase):
    def test_api(self):
        self.assertTrue(os.path.exists("recursive_find.py"),
                        "File recursive_find.py Does not exist.")
        import recursive_find
        self.assertTrue(hasattr(recursive_find, "BST"),
                        "BST is not defined")
        self.assertEqual(type(recursive_find.BST), type,
                         "BST is defined but it's not a class")

        from recursive_find import BST
        self.assertTrue(hasattr(BST, "add"),
                        "method add doesn't exist.")
        self.assertTrue(hasattr(BST, "find"),
                        "method find doesn't exist.")

    def test_simple(self):
        from recursive_find import BST
        b = BST()
        self.assertEqual(False, b.find(10),
                         "find(10) in empty BST should return False")

        b.add(10)
        self.assertEqual(True, b.find(10),
                         "find(10) on BST with just 10 added should return True")

        self.assertEqual(False, b.find(11),
                         "find(11) on BST with just 10 added should return False")

        b.add(17)
        b.add(25)
        b.add(36)
        self.assertTrue(b.find(17), "17 was added but not found")
        self.assertTrue(b.find(10), "10 was added but not found")
        self.assertTrue(b.find(25), "25 was added but not found")
        self.assertFalse(b.find(63), "63 was not added but found :/")


if __name__ == '__main__':
    main()
