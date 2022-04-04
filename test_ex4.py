import unittest
import ex4


'''
running example:
print([x for x in ex4.lazy_bounded_subset([1,2,5,4,3],4)])

[], [1], [2], [1, 2], [4], [3], [1, 3]

'''

# test lazy_bounded_subset:
class lazy_bounded_subsetTestCase(unittest.TestCase):
    def test_simple(self):
        # setUp
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cap = 9

        # Tests
        for i in ex4.bounded_subset(arr,cap):
            self.assertTrue(all(x in arr for x in i))
            self.assertLessEqual(sum(i), cap)

    def test_reverse(self):
        # setUp
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        cap = 9

        # Tests
        for i in ex4.bounded_subset(arr,cap):
            self.assertTrue(all(x in arr for x in i))
            self.assertLessEqual(sum(i), cap)

if __name__ == "__main__":
    unittest.main()
