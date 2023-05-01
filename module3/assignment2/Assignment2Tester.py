import unittest
from static_array import StaticArray
from dynamic_array import DynamicArray, find_mode
from bag_da import *


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

    def test_reduce(slf):
        da = DynamicArray([100])
        print(da.reduce(lambda x, y: x + y ** 2))
        print(da.reduce(lambda x, y: x + y ** 2, -1))
        da.remove_at_index(0)
        print(da.reduce(lambda x, y: x + y ** 2))
        print(da.reduce(lambda x, y: x + y ** 2, -1))

    def test_find_mode(self):
        test_cases = (
            [1, 1, 2, 3, 3, 4],
            [1, 2, 3, 4, 5],
            ["Apple", "Banana", "Banana", "Carrot", "Carrot", "Date", "Date", "Date",
             "Eggplant", "Eggplant", "Eggplant", "Fig", "Fig", "Grape"]
        )
        for case in test_cases:
            da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

        case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        da = DynamicArray()
        for x in range(len(case)):
            da.append(case[x])
            mode, frequency = find_mode(da)
            print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    # Bag methods testing
    def test_add(self):
        bag = Bag()
        print(bag)
        values = [10, 20, 30, 10, 20, 30]
        for value in values:
            bag.add(value)
        print(bag)

    def test_remove(self):
        bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
        print(bag)
        print(bag.remove(7), bag)
        print(bag.remove(3), bag)
        print(bag.remove(3), bag)
        print(bag.remove(3), bag)
        print(bag.remove(3), bag)

    def test_count(self):
        bag = Bag([1, 2, 3, 1, 2, 2])
        print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    def test_clear(self):
        bag = Bag([1, 2, 3, 1, 2, 3])
        print(bag)
        bag.clear()
        print(bag)

    def test_equal(self):
        bag1 = Bag([10, 20, 30, 40, 50, 60])
        bag2 = Bag([60, 50, 40, 30, 20, 10])
        bag3 = Bag([10, 20, 30, 40, 50])
        bag_empty = Bag()
        print(bag1, bag2, bag3, bag_empty, sep="\n")
        print(bag1.equal(bag2), bag2.equal(bag1))
        print(bag1.equal(bag3), bag3.equal(bag1))
        print(bag2.equal(bag3), bag3.equal(bag2))
        print(bag1.equal(bag_empty), bag_empty.equal(bag1))
        print(bag_empty.equal(bag_empty))
        print(bag1, bag2, bag3, bag_empty, sep="\n")
        bag1 = Bag([100, 200, 300, 200])
        bag2 = Bag([100, 200, 30, 100])
        print(bag1.equal(bag2))

    def test_dunder_iter(self):
        bag = Bag([5, 4, -8, 7, 10])
        print(bag)
        for item in bag:
            print(item)

    def test_dunder_next(self):
        bag = Bag(['orange', 'apple', 'pizza', 'icecream'])
        print(bag)
        for item in bag:
            print(item)