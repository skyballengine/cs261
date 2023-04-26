import unittest
from static_array import StaticArray
from assignment1 import min_max, fizz_buzz, reverse, rotate, sa_range, is_sorted, find_mode, remove_duplicates, \
    count_sort, transform_string


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

    def test_rotate_2(self):
        source = [_ for _ in range(-20, 20, 7)]
        arr = StaticArray(len(source))
        for i, value in enumerate(source):
            arr.set(i, value)
        print(arr)
        for steps in [1, 2, 0, -1, -2]:  # 28, -100, 2 ** 28, -2 ** 31]:
            if steps >= 0:
                space = " "
            else:
                space = ""
            print(f'{rotate(arr, steps)} {space} {steps}')
        print(arr)

    def test_sa_range(self):
        result = sa_range(1, 18)
        print(result)
        result_2 = sa_range(-1, 2)
        print(result_2)
        result_3 = sa_range(0, 0)
        print(result_3)
        result_4 = sa_range(-1202, -1206)
        print(result_4)
        result_5 = sa_range(0, -3)
        print(result_5)

    def test_is_sorted(self):
        asc_list = [_ for _ in range(1, 5)]
        desc_list = [_ for _ in range(15, 10, -1)]
        non_sorted_list = [1, 5, 2, 7, 8]
        sa_arr_asc = StaticArray(len(asc_list))
        sa_arr_desc = StaticArray(len(desc_list))
        sa_non_sorted = StaticArray(len(non_sorted_list))
        for i, value in enumerate(asc_list):
            sa_arr_asc.set(i, asc_list[i])
        for i, value in enumerate(desc_list):
            sa_arr_desc.set(i, desc_list[i])
        for i, value in enumerate(non_sorted_list):
            sa_non_sorted.set(i, non_sorted_list[i])
        asc_result = is_sorted(sa_arr_asc)
        desc_result = is_sorted(sa_arr_desc)
        non_sorted_result = is_sorted(sa_non_sorted)
        self.assertEqual(asc_result, 1)
        self.assertEqual(desc_result, -1)
        self.assertEqual(non_sorted_result, 0)
        ls = [-10, 0, 0, 10, 20, 30]
        sa_arr = StaticArray(len(ls))
        for i, value in enumerate(ls):
            sa_arr.set(i, ls[i])
        print(sa_arr)
        result = is_sorted(sa_arr)
        print(result)

    def test_find_mode(self):
        asc_list = [1, 2, 2, 3, 3, 3, 6, 6]
        desc_list = [9, 8, 6, 5, 4, 4, 4, 5, 5, 3, 3, 3, 3, 2]
        sa_arr_asc = StaticArray(len(asc_list))
        sa_arr_desc = StaticArray(len(desc_list))
        for i, value in enumerate(asc_list):
            sa_arr_asc.set(i, asc_list[i])
        for i, value in enumerate(desc_list):
            sa_arr_desc.set(i, desc_list[i])
        asc_result = find_mode(sa_arr_asc)
        desc_result = find_mode(sa_arr_desc)
        print(asc_result)
        print(desc_result)

    def test_remove_duplicates(self):
        asc_list = [1, 2, 2, 3, 3, 3, 6, 6]
        desc_list = [9, 8, 6, 5, 4, 4, 4, 3, 3, 3, 3, 2]
        sa_arr_asc = StaticArray(len(asc_list))
        sa_arr_desc = StaticArray(len(desc_list))
        for i, value in enumerate(asc_list):
            sa_arr_asc.set(i, asc_list[i])
        for i, value in enumerate(desc_list):
            sa_arr_desc.set(i, desc_list[i])
        print(sa_arr_asc)
        print(sa_arr_desc)
        asc_result = remove_duplicates(sa_arr_asc)
        desc_result = remove_duplicates(sa_arr_desc)
        print(asc_result)
        print(desc_result)

    def test_count_sort(self):
        ls = [5, 12, 11, 34, 3, 3, 32, 47, 21, 21]
        sa_ls = StaticArray(len(ls))
        for i, value in enumerate(ls):
            sa_ls[i] = value
        result = count_sort(sa_ls)
        print(result)

    def test_transform_string(self):
        test_cases = (
            'eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
            'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
            'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
            'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
            'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
            'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
            'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
            'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
            'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
            'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
            'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
        for case in test_cases:
            print(transform_string(case, '612HZ', '261TO'))


