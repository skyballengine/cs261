# Name: Eusebius Ballentine
# OSU Email: ballente@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 4-26-23
# Description: Python Fundamentals Review


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Function returns min and max of StaticArray
    """
    sa_min = arr[0]
    sa_max = arr[0]
    for i in range(arr.length()):
        if arr[i] < sa_min:
            sa_min = arr[i]
    for j in range(arr.length()):
        if arr[j] > sa_max:
            sa_max = arr[j]
    return sa_min, sa_max


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray of integers and returns a new StaticArray object
    with the content of the original array modified if certain conditions are met:
    1. If the number in the original array is divisible by 3, the corresponding element in the
    new array will be the string ‘fizz’.
    2. If the number in the original array is divisible by 5, the corresponding element in the
    new array will be the string ‘buzz’.
    3. If the number in the original array is both a multiple of 3 and a multiple of 5, the
    corresponding element in the new array will be the string ‘fizzbuzz’.
    4. In all other cases, the element in the new array will have the same value as in the
    original array.
    """
    new_sa_arr = StaticArray(arr.length())
    for n in range(arr.length()):
        if arr[n] % 15 == 0:
            new_sa_arr[n] = 'fizzbuzz'
        elif arr[n] % 3 == 0:
            new_sa_arr[n] = 'fizz'
        elif arr[n] % 5 == 0:
            new_sa_arr[n] = 'buzz'
        else:
            new_sa_arr[n] = arr[n]
    return new_sa_arr



# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Receives a StaticArray and reverses the order of the elements in the
    array, the reversal must be done ‘in place’
    """
    j = arr.length() - 1
    for i in range(arr.length()//2):
        temp = arr[i]
        arr[i] = arr[j-i]
        arr[j-i] = temp



# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Receives two parameters - a StaticArray and an integer value (called
    steps). The function will create and return a new StaticArray, which contains all of the
    elements from the original array, but their position has shifted right or left steps number of
    times.
    """
    sa_steps = abs(steps)
    len_arr = arr.length()
    sa_array = StaticArray(len_arr)
    if steps == 0:
        return arr

    if steps > 0:
        j = 0
        for i in range((len_arr - sa_steps) % len_arr, len_arr):
            sa_array[j] = arr[i]
            j += 1
        for i in range(0, (len_arr - sa_steps) % len_arr):
            sa_array[j] = arr[i]
            j += 1

    if steps < 0:
        j = 0
        for i in range(sa_steps % len_arr, len_arr):
            sa_array[j] = arr[i]
            j += 1
        for i in range(0, sa_steps % len_arr):
            sa_array[j] = arr[i]
            j += 1

    return sa_array


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Receives the two integers start and end, and returns a StaticArray that
    contains all the consecutive integers between start and end (inclusive).
    """
    sa_array = StaticArray(end - start + 1)
    j = start
    for i in range(sa_array.length()):
        sa_array.set(i, j)
        j += 1
    return sa_array



# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
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
