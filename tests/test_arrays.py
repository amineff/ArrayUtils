import unittest
import Array.Utils as ar

class TestArrays(unittest.TestCase):
    def test_sort_asending(self):
        random_array = ar.fill(30)
        sorted_array = ar.sort(random_array)
        print("random array", random_array)
        print("sorted array", sorted_array)
        self.assertNotEqual(random_array, ar.isSorted(sorted_array))
        print("min value:", ar.min(random_array))
        self.assertEqual(min(random_array),  ar.min(random_array))

if __name__ == '__main__':
    unittest.main()