import unittest
from static_array import StaticArray
from dynamic_array import DynamicArray
class Assignment2Tester(unittest.TestCase):

    def test_resize(self):
        da = DynamicArray()
        print(da)
        da.resize(da.get_capacity() * 2)
        print(da.get_capacity())
        print(da)
    def test_append(self):
        da = DynamicArray()
        da.append(4)
        print(da._data)
        for i in range(10):
            da.append(i)
        print(da)


    def test_insert_at_index(self):
        da = DynamicArray()
        print(da)
        da.insert_at_index(0, 4)
        print(da._data)
        print(da)
        da.insert_at_index(-1, 4)

    def test_remove_at_index(self):
        da = DynamicArray()
        print(da)
        da.append(4)
        print(da._data)
        for i in range(10):
            da.append(i)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        da.remove_at_index(1)
        print(da)
        print(da._data)

    def test_slice(self):
        da = DynamicArray([_ for _ in range(100)])
        print(da)
        new_da = da.slice(50, 33)
        print(new_da)

    def test_merge(self):
        da = DynamicArray([_ for _ in range(10)])
        new_da = DynamicArray([1, 2, 3, 4, 5, 6, 7])
        print(da)
        da.merge(new_da)
        print(da)


