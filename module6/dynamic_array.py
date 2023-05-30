# Name: Eusebius Ballentine
# OSU Email: ballente@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2a
# Due Date: May 1
# Description: Implement a Dynamic Array


from static_array import StaticArray
from random import random


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def get_data(self):
        return self._data

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def decrement_size(self):
        self._size -= 1

    def change_size(self, num):
        self._size += num

    def pop(self):
        self._data[self.length() - 1] = None
        self._size -= 1

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the underlying storage for the elements in the dynamic
        array. It does not change the values or the order of any elements currently stored in the
        array.
        """
        if new_capacity <= 0 or new_capacity < self._size:
            return
        new_sa_array = StaticArray(new_capacity)
        for i in range(self.length()):
            new_sa_array[i] = self._data[i]
        self._capacity = new_capacity
        self._data = new_sa_array

    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array. If the internal storage
        associated with the dynamic array is already full, you will need to DOUBLE its capacity
        before adding a new value using the function: resize
        """
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
            self._data[self._size] = value
            self._size += 1
        else:
            self._data[self._size] = value
            self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index in the dynamic array. Index 0 refers to
        the beginning of the array. If the provided index is invalid, the method raises a custom
        “DynamicArrayException”
        """
        if index < 0 or index > self._size:
            raise DynamicArrayException

        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        if self._size == 0:
            self._data[0] = value
            self._size += 1
            return

        for i in range(self.length(), index, -1):
            self._data[i] = self._data[i - 1]

        self._data.set(index, value)
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at the specified index in the dynamic array. Index 0
        refers to the beginning of the array. If the provided index is invalid, the method raises a
        custom “DynamicArrayException”

        When the number of elements stored in the array (before removal) is STRICTLY LESS than
        1/4 of its current capacity, the capacity must be reduced to TWICE the number of current
        elements. This check and capacity adjustment must occur BEFORE removal of the element.

        If the current capacity (before reduction) is 10 elements or less, reduction should not occur
        at all. If the current capacity (before reduction) is greater than 10 elements, the reduced
        capacity cannot become less than 10 elements. Please see the examples below, especially
        example #3, for clarification.
        """
        # validate index parameter
        if index < 0 or index >= self.length():
            raise DynamicArrayException

        # if _size equals 1, can remove single element in constant time (as noted in instructions)
        if self._size == 1:
            self._data[0] = None
            self._size -= 1

        elif self._size < self._capacity / 4 and self._capacity < 10:
            for i in range(index + 1, self._data.length()):
                self._data.set(i - 1, self._data[i])
            self._size -= 1

        # number of elements is less than 1/4 the capacity
        elif self._size < self._capacity / 4 and self._capacity > 10:

            # capacity is > 10 we WILL resize the array
            if self._size * 2 < 10:
                new_capacity = 10
            else:
                new_capacity = self._size * 2

            new_sa_array = StaticArray(new_capacity)
            for i in range(new_sa_array.length()):
                new_sa_array[i] = self._data[i]
            self._data = new_sa_array
            self._capacity = self._data.length()
            # element removal loop and decrement _size attribute
            for i in range(index + 1, self._data.length()):
                self._data.set(i - 1, self._data[i])
            self._size -= 1

        else:
            for i in range(index + 1, self._data.length()):
                self._data.set(i - 1, self._data[i])
            self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new DynamicArray object that contains the requested number of
        elements from the original array, starting with the element located at the requested start
        index. If the array contains N elements, a valid start_index is in range [0, N - 1] inclusive.
        A valid size is a non-negative integer.
        """
        # validate method parameters
        if size < 0 or start_index < 0 or start_index > self._size - 1 or size > self._size or (size + start_index) > self._size:
            raise DynamicArrayException

        new_da = DynamicArray()
        for i in range(start_index, start_index + size):
            new_da.append(self._data[i])
        return new_da

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Takes another DynamicArray object as a parameter, and appends all elements
        from this array onto the current one, in the same order in which they are stored in the input
        array.
        """
        for i in range(second_da.length()):
            self.append(second_da[i])

    def map(self, map_func) -> "DynamicArray":
        """
        Creates a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.
        """
        new_da_array = DynamicArray()
        for i in range(self._data.length()):
            if not self._data[i] is None:
                new_element = map_func(self._data[i])
                new_da_array.append(new_element)
        return new_da_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True.
        """
        new_da_array = DynamicArray()
        for i in range(self.length()):
            result = filter_func(self._data[i])
            if result:
                new_da_array.append(self._data[i])
        return new_da_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies the reduce_func to all elements of the dynamic array and
        returns the resulting value. It takes an optional initializer parameter. If this parameter is not
        provided, the first value in the array is used as the initializer. If the dynamic array is empty,
        the method returns the value of the initializer (or None, if one was not provided).
        """
        if initializer is None:
            initializer = self._data[0]
            for i in range(self.length() - 1):
                initializer = reduce_func(initializer, self._data[i + 1])
            return initializer
        if self.is_empty():
            return initializer
        initializer = reduce_func(initializer, self._data[0])
        for i in range(self.length() - 1):
            initializer = reduce_func(initializer, self._data[i + 1])
        return initializer


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Write a standalone function outside of the DynamicArray class that receives a dynamic array
    already in sorted order, either non-descending or non-ascending. The function will return a
    tuple containing (in this order) a dynamic array comprising the mode (most-occurring)
    value/s of the array, and an integer that represents the highest frequency (how many times
    they appear).
    If there is more than one value that has the highest frequency, all values at that frequency
    should be included in the array being returned in the order in which they appear in the input
    array. If there is only one mode, only that value should be included.
    """

    # mode dynamic array
    mode_da = DynamicArray()

    # assign variable: element to first element of arr
    element = arr[0]

    # assign variable: count to 1 because that is the minimum if the element is in arr
    count = 1
    # assign tuple: mode to first element with a count of 1
    mode = (element, count)
    mode_count = 0
    # if arr length is 1, then that is the mode
    if arr.length() == 1:
        mode_da.append(arr[0])
        return mode_da, count

    # assign variable: arr_len to arr.length() and use nested loop (I know I'm not supposed to, lol)
    arr_len = arr.length()
    # sample list [1, 1, 3, 3, 4, 4, 4, 5]
    mode_da.append(mode[0])
    arr_len = arr.length()
    for i in range(arr_len):
        # for each iteration count begins with 1
        current = arr[i]
        count = 1
        # for each element starting with variable: i, check if next element is equal, else break
        # count tracks number of occurrences
        for j in range(i, arr_len - 1):
            if arr[i] == arr[j + 1]:
                count += 1
            else:
                break
        # if current mode count is less than current count, then assign var: element to arr[i]
        # and redefine var: mode with new count value
        if count > mode[1]:
            for k in range(mode_da.length()):
                mode_da.remove_at_index(0)
            if mode_da.is_empty():
                mode_da.resize(4)
            element = arr[i]
            mode = (element, count)
            mode_da.append(arr[i])

        elif count == mode[1]:
            if mode_da.get_at_index(mode_da.length()-1) != arr[i]:
                mode_da.append(arr[i])

        # else:
        #     continue

    return mode_da, mode[1]

    # for i in range(arr_len):
    #     count = 1
    #     if arr[i] == arr[i+1]:
    #         count += 1
    #     if count > mode[1]:
    #         mode = (arr[i], count)
    #         mode_da.append(arr[i])
    # return mode_da, mode[1]





    # for i in range(arr_len):
    #     # for each iteration count begins with 1
    #     count = 1
    #     # for each element starting with variable: i, check if next element is equal, else break
    #     # count tracks number of occurrences
    #     for j in range(i, arr_len - 1):
    #         if arr[i] == arr[j + 1]:
    #             count += 1
    #         else:
    #             break
    #
    #     # if current mode count is less than current count, then assign var: element to arr[i]
    #     # and redefine var: mode with new count value
    #     if mode[1] < count:
    #         element = arr[i]
    #         mode = (element, count)
    # mode_da.append(mode[0])
    # return mode_da, mode[1]


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
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
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
