# Example of Binary Search on sorted list
# CS 261 / Oregon State University


def linear_search(list: list, target: object) -> int:
    """
    Searches for target, returns index where first found else -1
    Complexity:  O(n)  ["brute force" algorithm]
    """
    for i in range(len(list)):
        # once found, return index of first appearance and leave
        if list[i] == target:
            return i

    # we looked everywhere, we didn't see it - not found
    return -1


def selection_sort(list: list):
    """
    Sorts list in non-descending order
    Complexity:  O(n**2)
    """
    for i in range(len(list) - 1):
        min_index = i

        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        temp = list[min_index]
        list[min_index] = list[i]
        list[i] = temp


def binary_search(list: list, target: object) -> int:
    """
    Searches for target, returns index where first found else -1
    Complexity:  O(log n)
    Precondition:  List must be sorted in non-descending order
    """

    # set range of possible indices to entire list
    low = 0
    high = len(list) - 1

    while low <= high:

        # find the midpoint of all indices still possible
        mid = (low + high) // 2

        # Since value is lower, if it's there will be left of mid
        if target < list[mid]:
            high = mid - 1
        # Since value is higher, if it's there will be right of mid
        elif target > list[mid]:
            low = mid + 1
        # Neither higher not lower, it's a match - found
        else:
            return mid

    # All indices have been eliminated from consideration, not found
    return -1


# main for testing
some_list = [5, 2, 1, 8, 3, 12, 4, 7, 2, 6]

print("initial list:", some_list)
selection_sort(some_list)
print("sorted list:", some_list)

target = int(input('\nEnter a value to search for: '))

result = binary_search(some_list, target)

if result >= 0:
    print(target, 'was found at index ', result)
else:
    print(target, 'was not found in the list')


