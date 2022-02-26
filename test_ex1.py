import unittest
import ex1


# test safe args:
class safe_callTestCase(unittest.TestCase):
    # def setUp(self):
    #     pass

    def test_full_annotation(self):
        # setUp
        def f(a: int, b: float, c: str) -> list:
            return [str(a + b), c]

        # Tests
        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])

    def test_half_annotation(self):
        # setUp
        def f(a: int, b, c: str) -> list:
            return [str(a + b), c]
            
        # Tests
        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])

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
    def test_one_deep(self):
        # setUp
        l:list = [7, 5, 3, 2, 1, 4, 6, 9, 8]
        d:dict = {'c' : 9, 'a' : 5, 'b' : 4} # ans:  {'a' : 5, 'b' : 4, 'c' : 9}
        s:set = {7, 5, 3, 2, 1, 4, 6, 9, 8}
        t:tuple = (7, 5, 3, 2, 1, 4, 6, 9, 8)

        # Tests
        # list
        self.assertEqual(ex1.print_sorted(l), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        # dict
        self.assertEqual(ex1.print_sorted(d), {'a' : 5, 'b' : 4, 'c' : 9})
        # set
        self.assertEqual(ex1.print_sorted(s), {1, 2, 3, 4, 5, 6, 7, 8, 9})
        # tuple
        self.assertEqual(ex1.print_sorted(t), (1, 2, 3, 4, 5, 6, 7, 8, 9))

if __name__ == "__main__":
    unittest.main()
