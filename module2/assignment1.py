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
    # min and max both start as the first element of the static array
    sa_min = arr[0]
    sa_max = arr[0]
    # loop through to find min
    for i in range(arr.length()):
        if arr[i] < sa_min:
            sa_min = arr[i]
    # loop through to find max
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
    # create a new static array with the length of arr
    new_sa_arr = StaticArray(arr.length())
    # loop through to check if values are divisible by 15, 3, and 5 using modulo
    for n in range(arr.length()):
        # check 15 first
        if arr[n] % 15 == 0:
            new_sa_arr[n] = 'fizzbuzz'
        elif arr[n] % 3 == 0:
            new_sa_arr[n] = 'fizz'
        elif arr[n] % 5 == 0:
            new_sa_arr[n] = 'buzz'
        else:
            # simply add the value
            new_sa_arr[n] = arr[n]
    return new_sa_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Receives a StaticArray and reverses the order of the elements in the
    array, the reversal must be done ‘in place’
    """
    # give j the value of the last index
    j = arr.length() - 1
    # range should be divided by 2, swap will happen 1/2 as many times as the length of arr
    for i in range(arr.length() // 2):
        # swap
        temp = arr[i]
        arr[i] = arr[j - i]
        arr[j - i] = temp


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Receives two parameters - a StaticArray and an integer value (called
    steps). The function will create and return a new StaticArray, which contains all of the
    elements from the original array, but their position has shifted right or left steps number of
    times.
    """
    # sa_steps makes steps a positive integer
    sa_steps = abs(steps)
    len_arr = arr.length()
    sa_array = StaticArray(len_arr)

    # if no steps return arr
    if steps == 0:
        return arr

    # if steps is positive
    # use modulo for larger numbers
    # star
    if steps > 0:
        # use j as index for sa_array
        j = 0
        # build sa_array in two parts
        # part 1
        for i in range((len_arr - sa_steps) % len_arr, len_arr):
            sa_array[j] = arr[i]
            j += 1
        # part 2
        for i in range(0, (len_arr - sa_steps) % len_arr):
            sa_array[j] = arr[i]
            j += 1

    # if steps is negative
    # use modulo for larger numbers
    if steps < 0:
        # use j as index for sa_array
        j = 0
        # build sa_array in two parts
        # part 1
        for i in range(sa_steps % len_arr, len_arr):
            sa_array[j] = arr[i]
            j += 1
        # part 2
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
    # if start and end are equal, sa_array has a single value
    if start == end:
        sa_array = StaticArray(1)
        sa_array.set(0, start)
        return sa_array

    # if start and end are not equal, take absolute value of the difference + 1 as length of sa_array
    sa_array = StaticArray(abs(end - start) + 1)

    # if end greater than start, j will increment
    if end > start:
        j = start
        for i in range(sa_array.length()):
            sa_array.set(i, j)
            j += 1

    # if end greater than start, j will decrement
    if end < start:
        j = start
        for i in range(sa_array.length()):
            sa_array.set(i, j)
            j -= 1
    return sa_array


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Receives a StaticArray and returns an integer that describes whether
    the array is sorted. The method must return:
    ● 1 if the array is sorted in strictly ascending order.
    ● -1 if the list is sorted in strictly descending order.
    ● 0 otherwise.
    Arrays consisting of a single element are considered sorted in strictly ascending order.
    """
    arr_len = arr.length()
    # check if arr has a length of 1, if so return 1
    if arr_len == 1:
        return 1

    # check if first element is less than last element
    if arr[0] < arr[arr_len - 1]:
        for i in range(arr_len - 1):
            if arr.get(i) < arr.get(i + 1):
                continue
            else:
                return 0
        return 1

    # check if first element is greater than last element
    if arr[0] > arr[arr_len - 1]:
        for i in range(arr_len - 1):
            if arr.get(i) > arr.get(i + 1):
                continue
            else:
                return 0
        return -1


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    Receives a StaticArray that is sorted in order, either non-descending or
    non-ascending. The function will return, in this order, the mode (most-occurring value) of
    the array, and its frequency (how many times it appears).
    If there is more than one value that has the highest frequency, select the one that occurs
    first in the array.
    """
    # assign variable: element to first element of arr
    element = arr[0]

    # assign variable: count to 1 because that is the minimum if the element is in arr
    count = 1
    # assign tuple: mode to first element with a count of 1
    mode = (element, count)

    # if arr length is 1, then that is the mode
    if arr.length() == 1:
        return mode

    # assign variable: arr_len to arr.length() and use nested loop (I know I'm not supposed to, lol)
    arr_len = arr.length()
    for i in range(arr_len):
        # for each iteration count begins with 1
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
        if mode[1] < count:
            element = arr[i]
            mode = (element, count)
    return mode


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray that is already in sorted order, either
    non-descending or non-ascending. The function will return a new StaticArray with all
    duplicate values removed. The original array must not be modified.
    """
    arr_len = arr.length()

    # if length of arr is 1, initialize static array with length of 1 and single element of arr
    if arr_len == 1:
        sa_array = StaticArray(arr_len)
        sa_array.set(0, arr[0])
        return sa_array

    # var: count used to track occurrences of the value that each element holds
    count = 0
    for i in range(arr_len - 1):
        # increment var: count when the current element does not equal the following element
        if arr[i] != arr[i + 1]:
            count += 1
    # initialize static array with var: count number of elements + 1 to account for last element not counted
    sa_array = StaticArray(count + 1)
    # var: j to track indices of sa_array to set elements with values
    j = 0
    for i in range(arr_len - 1):
        if arr[i] != arr[i + 1]:
            sa_array.set(j, arr[i])
            j += 1
    # set last value that omitted from checks because of loop range
    sa_array.set(sa_array.length() - 1, arr[arr_len - 1])
    return sa_array


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray and returns a new StaticArray with the same
    content sorted in non-ascending order, using the count sort algorithm. The original array
    must not be modified.
    """

    arr_len = arr.length()

    # get min and max values
    min_and_max = min_max(arr)

    # build static array with function: sa_range from max to min (descending)
    sa_range_array = sa_range(min_and_max[1], min_and_max[0])
    count_sa_array = StaticArray(sa_range_array.length())
    final_sa_array = StaticArray(arr_len)

    for i in range(sa_range_array.length()):
        count = 0
        for j in range(arr_len):
            if arr[j] == sa_range_array[i]:
                count += 1
        count_sa_array[i] = count

    final_sa_array_index = 0

    for k in range(count_sa_array.length()):
        if count_sa_array[k] > 0:
            for p in range(count_sa_array[k]):
                final_sa_array.set(final_sa_array_index, sa_range_array[k])
                final_sa_array_index += 1

    return final_sa_array



# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    Receives three strings (source, s1, and s2) and returns a modified
    string that is the same length as source. The source string should be processed one
    character at a time, and the output string should be constructed according to these rules:
    1) If the character from the source string is present in s1 (any index), it should be
    replaced by the character at that same index in s2.
    2) Otherwise, if the character is:
    a) An uppercase letter -> replace with ' ' (a space)
    b) A lowercase letter -> replace with '#'
    c) A digit -> replace with '!'
    d) Anything else -> replace with '='
    """
    # initialize new empty string
    new_str = ''
    # loop through var: source string checking for conditions and concatenating onto var: new_str
    for i in range(len(source)):
        if source[i] in s1:
            s1_index = s1.index(source[i])
            new_str += s2[s1_index]
        elif source[i].isupper():
            new_str += " "
        elif source[i].islower():
            new_str += '#'
        elif source[i].isdigit():
            new_str += '!'
        else:
            new_str += '='
    return new_str


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
