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

    def test_map(self):
        da = DynamicArray([_ for _ in range(10)])
        print(da)
        print(da._data)
        def add_1(element):
            element += 1
            return element

        new_da_2 = DynamicArray()
        result = da.map(lambda x: (x ** 2))
        print(result)
        print(result._data)
        result_2 = result.map(add_1)
        print(result_2)

    def test_filter(self):
        def is_cool(element):
            if element < 5:
                return False
            else:
                return True
        da = DynamicArray([_ for _ in range(10)])
        print(da)
        print(da._data)
        result = da.filter(is_cool)
        print(result)

        def is_long_word(word, length):
            return len(word) > length

        da = DynamicArray("This is a sentence with some long words".split())
        print(da)
        for length in [3, 4, 7]:
            print(da.filter(lambda word: is_long_word(word, length)))

    def test_reduce(self):
        values = [100, 5, 10, 15, 20, 25]
        da = DynamicArray(values)
        print(da)
        print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
        print(da.reduce(lambda x, y: (x + y ** 2), -1))

