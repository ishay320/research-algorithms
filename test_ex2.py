import unittest
import ex2


# test last call:
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

# test List:
class ListTestCase(unittest.TestCase):
    def test_simple(self):
        # setUp
        mylist = ex2.List([
            [[1,2,3,33],[4,5,6,66]],
            [[7,8,9,99],[10,11,12,122]],
            [[13,14,15,155],[16,17,18,188]],
            ])

        # Tests
        self.assertEqual(mylist[0,1,3], 66)
        self.assertEqual(mylist[1], [[7, 8, 9, 99], [10, 11, 12, 122]])

if __name__ == "__main__":
    unittest.main()
