import random
from unittest import TestCase
from Sorting import sort

class Test(TestCase):
    def test_sort(self):
        # given
        arr = [15, 46, 88, 53, 24]
        arr1 = arr.copy()
        # when
        sort(arr)
        arr1.sort(reverse=True)
        # then
        self.assertEqual(arr, arr1)

    def test_sort_50_numbers(self):
        # given
        arr = random.sample(range(0, 999), 50)
        arr1 = arr.copy()
        # when
        sort(arr)
        arr1.sort(reverse=True)
        # then
        self.assertEqual(arr, arr1)
