import unittest
from static_array import StaticArray
from assignment1 import min_max, fizz_buzz, reverse, rotate


class Assignment1Tester(unittest.TestCase):
    def test_min_max(self):
        ls = [1, 5, 3, 9, -9, -100, 49, 32, 12, 0]
        sa_arr = StaticArray()
        for i in range(len(ls)):
            sa_arr.set(i, ls[i])
        print(sa_arr)
        result = min_max(sa_arr)
        print(result)
        for index in range(sa_arr.length()):
            print(sa_arr[index])
        self.assertEqual(result[0], -100)
        self.assertEqual(result[1], 49)

    def test_fizz_buzz(self):
        ls = [1, 5, 3, 9, -9, -100, 49, 32, 2, 15]
        sa_arr = StaticArray()
        for i in range(len(ls)):
            sa_arr.set(i, ls[i])
        result = fizz_buzz(sa_arr)
        print(result)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'buzz')
        self.assertEqual(result[2], 'fizz')
        self.assertEqual(result[9], 'fizzbuzz')

    def test_reverse(self):
        ls = [_ for _ in range(-10, 10, 2)]
        print(ls)
        sa_arr = StaticArray(len(ls))
        for i, value in enumerate(ls):
            sa_arr[i] = value
        print(sa_arr)
        reverse(sa_arr)
        print(sa_arr)
        self.assertEqual(sa_arr._data, reverse(ls))


    def test_rotate(self):
        ls = [_ for _ in range(-10, 10, 2)]
        print(ls)
        sa_arr = StaticArray(len(ls))
        for i, value in enumerate(ls):
            sa_arr[i] = value
        print(sa_arr)
        result = rotate(sa_arr, 2)
        print(result)
        sa_arr_2 = StaticArray(len(ls))
        for i, value in enumerate(ls):
            sa_arr_2[i] = value
        result_2 = rotate(sa_arr_2, -2)
        print(result_2)

