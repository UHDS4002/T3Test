import os.path
from unittest import TestCase


class TestMult(TestCase):
    def test_module_exists(self):
        self.assertTrue(os.path.exists('recursive_mult.py'))

    def test_api(self):
        import recursive_mult
        self.assertTrue(hasattr(recursive_mult, 'mult'),
                        "No Function Named 'mult' Defined In recursive_mult.py")
        self.assertTrue(recursive_mult.mult.__code__.co_argcount == 2,
                        "Function Must Have Two Parameters.")

    def test_simple(self):
        from recursive_mult import mult
        self.assertEqual(10, mult(2, 5), "mult(2,5) should be 10!")
        self.assertEqual(6, mult(1, 6), "mult(1,6) should be 6!")
        self.assertEqual(mult(7, 5), mult(5, 7),
                         "mult(5,7) should be equal to mult(7,5)!")





