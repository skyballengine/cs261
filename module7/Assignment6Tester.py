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
        # m = HashMap(23)
        # new_capacity = 1
        # while new_capacity < m._capacity or not m._is_prime(new_capacity):
        #     new_capacity = m._next_prime(new_capacity * 2)
        #     print(new_capacity)
        # m._capacity = new_capacity
        # print(m._capacity)

        print(f'Test 1')
        m = HashMap(11, hash_function_1)
        for i in range(5):
            m.put('str' + str(i), 100)
        print(m)
        m.resize_table(1)
        print(m)

        print(f'Test 2')
        m = HashMap(89, hash_function_1)
        for i in range(50):
            m.put('str' + str(i), 100)
        print(m)
        m.resize_table(2)
        print(m)

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

    def test_hash_function_1(self):
        hash = hash_function_1('str1')
        print(hash % 11)

        hash2 = hash_function_1('str2')
        print(hash2 % 11)

        hash3 = hash_function_1('some key')
        print(hash3 % 229)


    # Hash Table with Open Addressing

    def test_hash_function_1_and_2(self):
        m = HashMap(53, hash_function_2)
        print(m.get_capacity())
        print(hash_function_1('key164') % 53)
        print(hash_function_2('key164') % 53)
        # print(m.resize_table())
        hash3 = hash_function_1('some key')
        print(hash3)
        print(hash3 % 229)
        hash4 = hash_function_2('some key')
        print(hash4)
        print(hash4 % 229)

    def test_put_a(self):
        # print("\nPDF - put example 1")
        # print("-------------------")
        # m = HashMap(53, hash_function_1)
        # for i in range(150):
        #     m.put('str' + str(i), i * 100)
        #     print(f'Hash: {m._hash_function("str" + str(i)) % m.get_capacity()}')
        #     print(f'Iteration: {i}')
        #     print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
        #     print()

        print("\nPDF - put example 1")
        print("-------------------")
        m = HashMap(53, hash_function_1)
        for i in range(150):
            m.put('str' + str(i), i * 100)
            if i % 25 == 24:
                print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
        m.put('some key', 'some value')
        print(m.get_size())
        print(m.contains_key('some key'))
        print(m.get('some key'))
        m.remove('some key')
        print(m.get_size())
        print(m.contains_key('some key'))
        print(m.get('some key'))
        m.put('some key', 'some value')
        print(m.get_size())
        print(m.contains_key('some key'))
        print(m.get('some key'))


        # print("\nPDF - put example 2")
        # print("-------------------")
        # m = HashMap(41, hash_function_2)
        # for i in range(50):
        #     m.put('str' + str(i // 3), i * 100)
        #     if i % 10 == 9:
        #         print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())


    def test_put_hash_1(self):
        print("\nPDF - put example 1")
        m = HashMap(53, hash_function_1)
        # for i in range(15):
        #     m.put('str' + str(i), i * 100)
        #     print(m)
        # print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
        print(hash_function_1('str14') % 53)
        print(hash_function_2('str14') % 53)
        print(hash_function_1('str12') % 41)
        print(hash_function_2('str12') % 41)

    def test_put_hash_2(self):
        print("\nPDF - put example 2")
        m = HashMap(53, hash_function_2)
        for i in range(15):
            m.put('str' + str(i), i * 100)
            print(m)
        print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
        print(hash_function_1('str14') % 53)
        print(hash_function_2('str14') % 53)

    def test_empty_buckets_a(self):
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


    def test_table_load_a(self):
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

    def test_clear_a(self):
        pass

    def test_resize_table_a(self):
        # print("\nPDF - resize example 1")
        # print("----------------------")
        # m = HashMap(20, hash_function_1)
        # m.put('key1', 10)
        # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
        # m.resize_table(30)
        # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
        #
        # print("\nPDF - resize example 2")
        # print("----------------------")
        # m = HashMap(75, hash_function_2)
        # keys = [i for i in range(25, 1000, 13)]
        # for key in keys:
        #     m.put(str(key), key * 42)
        #     # print(f'Key: {key} Contains key: {m.contains_key(str(key))}')
        # print(m.get_size(), m.get_capacity())
        #
        # for capacity in range(111, 1000, 117):
        #     m.resize_table(capacity)
        #
        #     if m.table_load() > 0.5:
        #         print(f"Check that the load factor is acceptable after the call to resize_table().\n"
        #               f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")
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

        m = HashMap(229, hash_function_1)
        m.put("some key", "some value")
        print(m)
    def test_get_a(self):
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

    def test_contains_key_a(self):
        print("\nPDF - contains_key example 1")
        print("----------------------------")
        m = HashMap(11, hash_function_1)
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

    def test_remove_a(self):
        print("\nPDF - remove example 1")
        print("----------------------")
        m = HashMap(53, hash_function_1)
        print(m.get('key1'))
        m.put('key1', 10)
        print(m.get('key1'))
        m.remove('key1')
        print(m.get('key1'))
        m.remove('key4')

    def test_get_keys_and_values_a(self):
        pass

    def test_iter_a(self):
        print("\nPDF - __iter__(), __next__() example 1")
        print("---------------------")
        m = HashMap(10, hash_function_1)
        for i in range(5):
            m.put(str(i), str(i * 10))
        print(m)
        for item in m:
            print('K:', item.key, 'V:', item.value)

    def test_next_a(self):
        print("\nPDF - __iter__(), __next__() example 2")
        print("---------------------")
        m = HashMap(10, hash_function_2)
        for i in range(5):
            m.put(str(i), str(i * 24))
        m.remove('0')
        m.remove('4')
        print(m)
        for item in m:
            print('K:', item.key, 'V:', item.value)





