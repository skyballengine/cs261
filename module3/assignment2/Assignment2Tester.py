import unittest
from static_array import StaticArray, StaticArrayException
from dynamic_array import DynamicArray, find_mode
from bag_da import *


class Assignment2Tester(unittest.TestCase):

    def test_resize(self):
        da = DynamicArray()

        # print dynamic array's size, capacity and the contents
        # of the underlying static array (data)
        da.print_da_variables()
        da.resize(8)
        da.print_da_variables()
        da.resize(2)
        da.print_da_variables()
        self.assertRaises(StaticArrayException, da.resize, 0)

    def test_append(self):
        da = DynamicArray()
        da.append(4)
        print(da._data)
        for i in range(10):
            da.append(i)
        print(da)

    def test_insert_at_index(self):
        # da = DynamicArray([100])
        # print(da)
        # da.insert_at_index(0, 200)
        # da.insert_at_index(0, 300)
        # da.insert_at_index(0, 400)
        # print(da)
        # da.insert_at_index(3, 500)
        # print(da)
        # da.insert_at_index(1, 600)
        # print(da)
        # da = DynamicArray()
        # try:
        #     da.insert_at_index(-1, 100)
        # except Exception as e:
        #     print("Exception raised:", type(e))
        # da.insert_at_index(0, 200)
        # try:
        #     da.insert_at_index(2, 300)
        # except Exception as e:
        #     print("Exception raised:", type(e))
        # print(da)
        da = DynamicArray()
        for i in range(1, 10):
            index, value = i - 4, i * 10
            try:
                da.insert_at_index(index, value)
            except Exception as e:
                print("Cannot insert value", value, "at index", index)
        print(da)

    def test_remove_at_index(self):
        # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
        # print(da)
        # da.remove_at_index(0)
        # print(da)
        # da.remove_at_index(6)
        # print(da)
        # da.remove_at_index(2)
        # print(da)
        #
        # da = DynamicArray([1024])
        # print(da)
        # for i in range(17):
        #     da.insert_at_index(i, i)
        # print(da.length(), da.get_capacity())
        # for i in range(16, -1, -1):
        #     da.remove_at_index(0)
        # print(da)

        # da = DynamicArray()
        # print(da.length(), da.get_capacity())
        # [da.append(1) for i in range(100)]  # step 1 - add 100 elements
        # print(da.length(), da.get_capacity())
        # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
        # print(da.length(), da.get_capacity())
        # da.remove_at_index(0)  # step 3 - remove 1 element
        # print(da.length(), da.get_capacity())
        # da.remove_at_index(0)  # step 4 - remove 1 element
        # print(da.length(), da.get_capacity())
        # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
        # print(da.length(), da.get_capacity())
        # da.remove_at_index(0)  # step 6 - remove 1 element
        # print(da.length(), da.get_capacity())
        # da.remove_at_index(0)  # step 7 - remove 1 element
        # print(da.length(), da.get_capacity())
        # for i in range(14):
        #     print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        #     da.remove_at_index(0)
        #     print(" After remove_at_index(): ", da.length(), da.get_capacity())
        da = DynamicArray([1, 2, 3, 4, 5])
        print(da)
        for _ in range(5):
            da.remove_at_index(0)
            print(da)
    def test_slice(self):
        # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # da_slice = da.slice(1, 3)
        # print(da, da_slice, sep="\n")
        # da_slice.remove_at_index(0)
        # print(da, da_slice, sep="\n")
        da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
        print("SOURCE:", da)
        slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
        for i, cnt in slices:
            print("Slice", i, "/", cnt, end="")
            try:
                print(" --- OK: ", da.slice(i, cnt))
            except:
                print(" --- exception occurred.")

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
        def filter_a(e):
            return e > 10

        da = DynamicArray([1, 5, 10, 15, 20, 25])
        print(da)
        result = da.filter(filter_a)
        print(result)
        print(da.filter(lambda x: (10 <= x <= 20)))

        # def is_long_word(word, length):
        #     return len(word) > length
        #
        # da = DynamicArray("This is a sentence with some long words".split())
        # print(da)
        # for length in [3, 4, 7]:
        #     print(da.filter(lambda word: is_long_word(word, length)))

    def test_reduce(slf):
        da = DynamicArray([100])
        print(da.reduce(lambda x, y: x + y ** 2))
        print(da.reduce(lambda x, y: x + y ** 2, -1))
        da.remove_at_index(0)
        print(da.reduce(lambda x, y: x + y ** 2))
        print(da.reduce(lambda x, y: x + y ** 2, -1))

    def test_find_mode(self):
        # test_cases = (
        #     [1, 1, 2, 3, 3, 4],
        #     [1, 2, 3, 4, 5],
        #     ["Apple", "Banana", "Banana", "Carrot", "Carrot", "Date", "Date", "Date",
        #      "Eggplant", "Eggplant", "Eggplant", "Fig", "Fig", "Grape"]
        # )
        # for case in test_cases:
        #     da = DynamicArray(case)
        #     mode, frequency = find_mode(da)
        #     print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

        case = [-963]
        da = DynamicArray(case)
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
        # bag1 = Bag([10, 20, 30, 40, 50, 60])
        # bag2 = Bag([60, 50, 40, 30, 20, 10])
        # bag3 = Bag([10, 20, 30, 40, 50])
        # bag_empty = Bag()
        # print(bag1, bag2, bag3, bag_empty, sep="\n")
        # print(bag1.equal(bag2), bag2.equal(bag1))
        # print(bag1.equal(bag3), bag3.equal(bag1))
        # print(bag2.equal(bag3), bag3.equal(bag2))
        # print(bag1.equal(bag_empty), bag_empty.equal(bag1))
        # print(bag_empty.equal(bag_empty))
        # print(bag1, bag2, bag3, bag_empty, sep="\n")
        # bag1 = Bag([100, 200, 300, 200])
        # bag2 = Bag([100, 200, 30, 100])
        # print(bag1.equal(bag2))
        bag1 = Bag([-87677, 88830, 95285, -40302, -20746, 51222])
        bag2 = Bag([-20746, -40302, -76271, 28797, -44254, -80330])
        for i in range(bag1._da.length()):
            print(bag1.count(bag1._da[i]))
        for i in range(bag2._da.length()):
            print(bag2.count(bag2._da[i]))
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