import unittest
import ex1


# test safe args:
class safe_callTestCase(unittest.TestCase):
    def test_full_annotation(self):
        # setUp
        def f(a: int, b: float, c: str) -> list:
            return [str(a + b), c]

        # Tests
        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])
        with self.assertRaises(TypeError):
             ex1.safe_call(f, c=1, b=1.2, a=1)

    def test_half_annotation(self):
        # setUp
        def f(a: int, b, c: str) -> list:
            return [str(a + b), c]
            
        # Tests
        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])
        with self.assertRaises(TypeError):
             ex1.safe_call(f, c=1, b=1.2, a=1)

    def test_no_annotation(self):
        # setUp
        def f(a, b, c):
            return [str(a + b), c]
            
        # Tests
        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])

# test print sorted:
class print_sortedTestCase(unittest.TestCase):
    def setUp(self):
        self.l:list = [7, 5, 3, 2, 1, 4, 6, 9, 8]
        self.d:dict = {'c' : 9, 'a' : 5, 'b' : 4} # ans:  {'a' : 5, 'b' : 4, 'c' : 9}
        self.s:set = {7, 5, 3, 2, 1, 4, 6, 9, 8}
        self.t:tuple = (7, 5, 3, 2, 1, 4, 6, 9, 8)

    def test_one_deep(self):
        # list
        self.assertEqual(ex1.print_sorted(self.l), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        # dict
        self.assertEqual(ex1.print_sorted(self.d), {'a' : 5, 'b' : 4, 'c' : 9})
        # set
        self.assertEqual(ex1.print_sorted(self.s), {1, 2, 3, 4, 5, 6, 7, 8, 9})
        # tuple
        self.assertEqual(ex1.print_sorted(self.t), (1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_two_deep(self):
        new_d = {'c' : self.t, 'a' : self.s, 'b' : self.l}
        self.assertEqual(ex1.print_sorted(new_d), {'a' : {1, 2, 3, 4, 5, 6, 7, 8, 9}, 'b' : [1, 2, 3, 4, 5, 6, 7, 8, 9], 'c' : (1, 2, 3, 4, 5, 6, 7, 8, 9)})

    def test_three_deep(self):
        new_d = {'c' : {'c' : self.t, 'a' : 5, 'b' : 4}, 'a' : self.s, 'b' : self.l}
        self.assertEqual(ex1.print_sorted(new_d), {'a' : {1, 2, 3, 4, 5, 6, 7, 8, 9}, 'b' : [1, 2, 3, 4, 5, 6, 7, 8, 9], 'c' : {'a' : 5, 'b' : 4, 'c' : (1, 2, 3, 4, 5, 6, 7, 8, 9)}})


if __name__ == "__main__":
    unittest.main()
