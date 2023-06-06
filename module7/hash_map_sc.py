# Name: Eusebius Ballentine
# OSU Email: ballente@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 6
# Due Date: 06-09-23
# Description: Hash Map With Separate Chaining


from a6_include import (DynamicArray, LinkedList, LinkedListIterator,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def get_buckets(self) -> DynamicArray:
        """
        Return underlying DynamicArray
        """
        return self._buckets

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map. If the given key already exists in
        the hash map, its associated value must be replaced with the new value. If the given key is
        not in the hash map, a new key/value pair must be added.

        For this hash map implementation, the table must be resized to double its current
        capacity when this method is called and the current load factor of the table is
        greater than or equal to 1.0.
        """
        # if necessary resize table
        if self.table_load() >= 1:
            self.resize_table(self._capacity * 2)
            # self.resize_table(self._capacity)

        # find index by calling hash function on key
        arr_index = self._hash_function(key) % self._capacity

        # get linked list
        linked_list = self._buckets[arr_index]

        # validate whether key already exists, if so overwrite value of key, else add to linked list
        node = linked_list.contains(key)

        # if node is None add node with key and value
        if node is None:
            linked_list.insert(key, value)
            self._size += 1

        # else overwrite with new value
        else:
            node.value = value

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table.
        """
        empty_buckets_count = 0
        for _ in range(self._capacity):
            if self._buckets[_].length() == 0:
                empty_buckets_count += 1
        return empty_buckets_count

    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        Clears the contents of the hash map. It does not change the underlying hash
        table capacity.
        """
        for _ in range(self._capacity):
            self._buckets[_] = LinkedList()
        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table. All existing key/value pairs
        must remain in the new hash map, and all hash table links must be rehashed. (Consider
        calling another HashMap method for this part).

        First check that new_capacity is not less than 1; if so, the method does nothing.
        If new_capacity is 1 or more, make sure it is a prime number. If not, change it to the next
        highest prime number. You may use the methods _is_prime() and _next_prime() from the
        skeleton code.
        """
        # print(self._buckets)
        if new_capacity < 1:
            return

        # while new_capacity < self._capacity or not self._is_prime(new_capacity):
        #     new_capacity = self._next_prime(new_capacity * 2)
        #
        # self._capacity = new_capacity

        # # same condition as in put()
        # if self.table_load() >= 1:
        #     self._capacity = self._next_prime(new_capacity)
        # #
        # # else:
        # #     while new_capacity < self._capacity or not self._is_prime(new_capacity):
        # #         new_capacity = self._next_prime(new_capacity * 2)
        # #     self._capacity = new_capacity
        #
        # # check if new_capacity is prime, if so assign as self._capacity
        # if self._is_prime(new_capacity):
        #     # new_prime_capacity = self._next_prime(new_capacity)
        #     # resize creating a new hash table with new capacity and old values
        #     self._capacity = new_capacity
        # # validation for using resize independently of put
        # else:
        #     self._capacity = self._next_prime(new_capacity)

        # # same condition as in put()
        if self.table_load() >= 1:
            self._capacity = self._next_prime(new_capacity)
        #
        # else:
        #     while new_capacity < self._capacity or not self._is_prime(new_capacity):
        #         new_capacity = self._next_prime(new_capacity * 2)
        #     self._capacity = new_capacity

        # check if new_capacity is prime, if so assign as self._capacity
        # validation for using resize independently of put
        else:
            self._capacity = self._next_prime(new_capacity)

        new_da = DynamicArray()
        for _ in range(self._capacity):
            # append a LinkedList for each iteration index 0 - self._capacity - 1
            new_da.append(LinkedList())
        # for each index of the da length
        # for i in range(self._buckets.length()):
        for i in range(self._buckets.length()):
            # if any nodes in the linked list?
            if self._buckets[i].length() == 0:
                continue
            else:
                ll_iterator = iter(self._buckets[i])
                # rerun each key through the hash function
                for j in range(self._buckets[i].length()):
                    node = next(ll_iterator)
                    new_hash_index = self._hash_function(node.key) % self._capacity
                    new_da[new_hash_index].insert(node.key, node.value)

        self._buckets = new_da

        # print(f'Dynamic Array Length: {self._buckets.length()}')
        # print(f'self._capacity: {self._capacity}')

        # # print(self._buckets)
        # if new_capacity < 1:
        #     return
        # else:
        #     # new_prime_capacity = self._next_prime(new_capacity)
        #     # resize creating a new hash table with new capacity and old values
        #
        #     self._capacity = self._next_prime(new_capacity)
        # new_da = DynamicArray()
        # for _ in range(self._capacity):
        #     # append a LinkedList for each iteration index 0 - self._capacity - 1
        #     new_da.append(LinkedList())
        # # for each index of the da length
        # # for i in range(self._buckets.length()):
        # for i in range(self._buckets.length()):
        #     # if any nodes in the linked list?
        #     if self._buckets[i].length() == 0:
        #         continue
        #     else:
        #         ll_iterator = iter(self._buckets[i])
        #         # rerun each key through the hash function
        #         for j in range(self._buckets[i].length()):
        #             node = next(ll_iterator)
        #             new_hash_index = self._hash_function(node.key) % self._capacity
        #             new_da[new_hash_index].insert(node.key, node.value)
        #
        # self._buckets = new_da
        #
        # print(f'Dynamic Array Length: {self._buckets.length()}')
        # print(f'self._capacity: {self._capacity}')

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key. If the key is not in the hash
        map, the method returns None.
        """
        arr_index = self._hash_function(key) % self._capacity
        linked_list = self._buckets[arr_index]
        if linked_list.length() == 0:
            return

        ll_iterator = iter(linked_list)
        for i in range(linked_list.length()):
            node = next(ll_iterator)
            if node.key == key:
                return node.value

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map, otherwise it returns False. An
        empty hash map does not contain any keys.
        """
        if self._size == 0:
            return False

        arr_index = self._hash_function(key) % self._capacity
        linked_list = self._buckets[arr_index]
        if linked_list.length() == 0:
            return False

        ll_iterator = iter(linked_list)
        for i in range(linked_list.length()):
            node = next(ll_iterator)
            if node.key == key:
                return True
        return False

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the hash map. If the key
        is not in the hash map, the method does nothing (no exception needs to be raised).
        """
        arr_index = self._hash_function(key) % self._capacity
        linked_list = self._buckets[arr_index]
        if linked_list.length() == 0:
            return

        if linked_list.contains(key):
            linked_list.remove(key)
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a dynamic array where each index contains a tuple of a key/value pair
        stored in the hash map. The order of the keys in the dynamic array does not matter.
        """
        new_da = DynamicArray()
        for _ in range(self._buckets.length()):
            linked_list = self._buckets[_]
            ll_iterator = iter(linked_list)
            for i in range(linked_list.length()):
                node = next(ll_iterator)
                new_da.append((node.key, node.value))
        return new_da


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Receives a dynamic array(that is not guaranteed to be sorted). This function will return a tuple containing, in this
    order, a dynamic array comprising the mode (most occurring) value/s of the array, and an
    integer that represents the highest frequency (how many times the mode value(s) appear).
    If there is more than one value with the highest frequency, all values at that frequency
    should be included in the array being returned (the order does not matter). If there is only
    one mode, the dynamic array will only contain that value.

    You may assume that the input array will contain at least one element, and that all values
    stored in the array will be strings. You do not need to write checks for these conditions.
    For full credit, the function must be implemented with O(N) time complexity. For best
    results, we recommend using the separate chaining hash map provided for you in the
    function’s skeleton code.
    """

    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    mode_map = HashMap(capacity=da.length())
    mode_map_buckets = mode_map.get_buckets()

    # # if necessary resize table
    # if mode_map.table_load() >= 1:
    #     mode_map.resize_table(mode_map.get_capacity() * 2)

    # create a da for storing the mode(s) of the original da will return at the end of the function
    mode_da = DynamicArray()

    # if da has only one value
    if da.length() == 1:
        mode_da.append(da[0])
        return mode_da, 1

    # need a new put operation that inserts a new SLNode with new key
    # or increments the value of the SLNode with existing key

    # add all values from da into HashMap by key incrementing the value in the node each time key is overwritten
    for i in range(da.length()):
        arr_index = hash_function_1(da[i]) % mode_map.get_capacity()
        linked_list = mode_map_buckets[arr_index]
        node_value = mode_map.get(da[i]) if linked_list.contains(da[i]) else 1
        node = linked_list.contains(da[i])

        if node:
            node.value = node_value + 1

        else:
            linked_list.insert(da[i], node_value)

    mode_count = 0
    keys_and_values_da = mode_map.get_keys_and_values()
    for j in range(keys_and_values_da.length()):
        if keys_and_values_da[j][1] > mode_count:
            mode_count = keys_and_values_da[j][1]

    for k in range(keys_and_values_da.length()):
        if keys_and_values_da[k][1] == mode_count:
            mode_da.append(keys_and_values_da[k][0])

    return mode_da, mode_count



# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
