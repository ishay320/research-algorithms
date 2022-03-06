import unittest
import ex2


# test safe args:
class lastcallTestCase(unittest.TestCase):
    def test_simple(self):
        # setUp
        @ex2.lastcall
        def sqr(x:int) -> int:
            return x**2

        # Tests
        self.assertEqual(sqr(2),4)
        self.assertEqual(sqr(2),"I already told you that the answer is 4!")
        self.assertEqual(sqr(4),16)
        self.assertEqual(sqr(4),"I already told you that the answer is 16!")

        # check if remember only last
        self.assertEqual(sqr(2),4)

    def test_complex(self):
        # setUp
        @ex2.lastcall
        def fillList(start:int,end:int,fill:str) -> list[str]:
            return [fill for _ in range(start,end)] 

        # Tests
        self.assertEqual(fillList(1, 5, "Hi"),['Hi', 'Hi', 'Hi', 'Hi'])
        self.assertEqual(fillList(1, 5, "Hi"),"I already told you that the answer is ['Hi', 'Hi', 'Hi', 'Hi']!")
        self.assertEqual(fillList(3, 4, ";)"), [";)"])
        self.assertEqual(fillList(3, 4, ";)"),"I already told you that the answer is [';)']!")

        # check if remember only last
        self.assertEqual(fillList(1, 5, "Hi"),['Hi', 'Hi', 'Hi', 'Hi'])


if __name__ == "__main__":
    unittest.main()
