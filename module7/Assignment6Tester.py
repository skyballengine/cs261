import unittest
from hash_map_sc import *
# from hash_map_oa import *
from a6_include import *


class Assignment6Tester(unittest.TestCase):

    # Hash Table with Separate Chaining
    def test_put_c(self):
        print("\nPDF - put example 1")
        print("-------------------")
        m = HashMap(53, hash_function_1)
        for i in range(55):
            m.put('str' + str(i), i * 100)
            print(m)
            if i % 25 == 24:
                print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())



    def test_empty_buckets_c(self):
        pass

    def test_table_load_c(self):
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

    def test_clear_c(self):
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

    def test_is_prime_c(self):
        pass

    def test_next_prime_c(self):
        h = HashMap()
        print(h._next_prime(23))
    def test_resize_table_c(self):
        # print("\nPDF - resize example 1")
        # print("----------------------")
        # m = HashMap(23, hash_function_1)
        # m.put('key1', 10)
        # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
        # m.resize_table(30)
        # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

        # print("\nPDF - resize example 2")
        # print("----------------------")
        # m = HashMap(79, hash_function_2)
        # keys = [i for i in range(1, 1000, 13)]
        # for key in keys:
        #     m.put(str(key), key * 42)
        # print(m.get_size(), m.get_capacity())
        #
        # for capacity in range(111, 1000, 117):
        #     m.resize_table(capacity)
        #
        #     m.put('some key', 'some value')
        #     result = m.contains_key('some key')
        #     m.remove('some key')
        #
        #     for key in keys:
        #         # all inserted keys must be present
        #         result &= m.contains_key(str(key))
        #         # NOT inserted keys must be absent
        #         result &= not m.contains_key(str(key + 1))
        #     print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))
        m = HashMap(23)
        new_capacity = 1
        while new_capacity < m._capacity or not m._is_prime(new_capacity):
            new_capacity = m._next_prime(new_capacity * 2)
            print(new_capacity)
        m._capacity = new_capacity
        print(m._capacity)


    def test_get_c(self):
        print("\nPDF - get example 1")
        print("-------------------")
        m = HashMap(31, hash_function_1)
        print(m.get('key'))
        m.put('key1', 10)
        print(m.get('key1'))

    def test_contains_key_c(self):
        # print("\nPDF - contains_key example 1")
        # print("----------------------------")
        # m = HashMap(53, hash_function_1)
        # print(m.contains_key('key1'))
        # m.put('key1', 10)
        # m.put('key2', 20)
        # m.put('key3', 30)
        # print(m.contains_key('key1'))
        # print(m.contains_key('key4'))
        # print(m.contains_key('key2'))
        # print(m.contains_key('key3'))
        # m.remove('key3')
        # print(m.contains_key('key3'))

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

    def test_remove_c(self):
        pass

    def test_get_keys_and_values_c(self):
        pass

    def test_find_mode_c(self):
        # print("\nPDF - find_mode example 1")
        # print("-----------------------------")
        # da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
        # print(find_mode(da))
        # # print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

        # print("\nPDF - find_mode example 2")
        # print("-----------------------------")
        # test_cases = (
        #     ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        #     ["one", "two", "three", "four", "five"],
        #     ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
        # )
        #
        # for case in test_cases:
        #     da = DynamicArray(case)
        #     print(find_mode(da))

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


    def test_hash_function_1(self):
        hash = hash_function_1('str1')
        print(hash % 11)

        hash2 = hash_function_1('str2')
        print(hash2 % 11)
    def test_iter_c(self):
        m = HashMap()
        m.put(7, 6)
        m.put(18, 7)
        print(m)
        print(m._buckets[7])
        ll = m._buckets[7]
        ll_iter = iter(ll)
        print(ll_iter)
        print(next(ll_iter))
        print(next(ll_iter))
        print(next(ll_iter))

        ll_iter_2 = iter(ll)
        while True:
            print(next(ll_iter_2))



    # Hash Table with Open Addressing

    def test_put_a(self):
        pass

    def test_empty_buckets_a(self):
        pass

    def test_table_load_a(self):
        pass

    def test_clear_a(self):
        pass

    def test_resize_table_a(self):
        pass

    def test_get_a(self):
        pass

    def test_contains_key_a(self):
        pass

    def test_remove_a(self):
        pass

    def test_get_keys_and_values_a(self):
        pass

    def test_iter_a(self):
        pass

    def test_next_a(self):
        pass





