import unittest
import ex1


# test safe args:
class safe_callTestCase(unittest.TestCase):
    # def setUp(self):
    #     pass

    def test_full_annotation(self):
        def f(a: int, b: float, c: str) -> list:
            return [str(a + b), c]

        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])


    def test_half_annotation(self):
        def f(a: int, b, c: str) -> list:
            return [str(a + b), c]

        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])

    def test_no_annotation(self):
        def f(a, b, c):
            return [str(a + b), c]

        self.assertEqual(ex1.safe_call(f, a=1, b=1.2, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, b=1.2, a=1, c="string"), ["2.2", "string"])
        self.assertEqual(ex1.safe_call(f, c="string", b=1.2, a=1), ["2.2", "string"])


if __name__ == "__main__":
    unittest.main()
