# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining heap property.
        The runtime complexity of this implementation must be O(log N).
        """
        # if heap is empty append node value to the da as root
        if self._heap.is_empty():
            self._heap.append(node)
            return

        # if heap is not empty
        self._heap.append(node)
        # create variables for tracking indexes
        node_index = self._heap.length() - 1
        parent_node_index = (node_index - 1) // 2
        parent_tracker = parent_node_index
        while True:
            if parent_tracker == 0 and self._heap[node_index] < self._heap[parent_tracker]:
                temp = self._heap[parent_tracker]
                self._heap[parent_tracker] = node
                self._heap[node_index] = temp
                break

            elif self._heap[node_index] < self._heap[parent_tracker]:
                temp = self._heap[parent_tracker]
                self._heap[parent_tracker] = node
                self._heap[node_index] = temp
                node_index = parent_tracker
                parent_tracker = (node_index - 1) // 2

            else:
                break
        return

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty; otherwise, it returns False.
        The runtime complexity of this implementation must be O(1).
        """
        return self._heap.is_empty()

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        The runtime complexity of this implementation must be O(1).
        """
        if self._heap.is_empty():
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Returns an object with the minimum key, and removes it from the heap. If the
        heap is empty, the method raises a MinHeapException.
        For the downward percolation of the replacement node: if both children of the node have
        the same value (and are both smaller than the node), swap with the left child.
        The runtime complexity of this implementation must be O(log N).
        """
        if self.is_empty():
            raise MinHeapException

        if self.size() == 1:
            value = self._heap[0]
            self._heap[0] = None
            self._heap.decrement_size()
            return value
        # define value to be removed; the min value
        removed_node = self._heap[0]

        # find last node's index
        last_node_index = self.size() - 1

        # replace first node with last node and remove last node
        self._heap[0] = self._heap[last_node_index]
        self._heap[last_node_index] = None
        self._heap.decrement_size()

        # percolate the node down to its proper location as per the qualities of a min heap
        node_index = 0
        # print(node)
        _percolate_down(self._heap, node_index)
        return removed_node

        # if self.is_empty():
        #     raise MinHeapException
        #
        # if self.size() == 1:
        #     value = self._heap[0]
        #     self._heap[0] = None
        #     self._heap._size -= 1
        #     return value
        # # define value to be removed; the min value
        # removed_node = self._heap[0]
        #
        # # find last node's index
        # last_node_index = self.size() - 1
        #
        # # replace first node with last node and remove last node
        # self._heap[0] = self._heap[last_node_index]
        # self._heap[last_node_index] = None
        # self._heap._size -= 1
        #
        # # percolate the node down to its proper location as per the qualities of a min heap
        # node = self._heap[0]
        # # print(node)
        # _percolate_down(self._heap, node)
        # return removed_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order, and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        The runtime complexity of this implementation must be O(N). If the runtime complexity is
        O(N log N), you will not receive any points for this portion of the assignment, even if your
        method passes Gradescope.
        """
        self.clear()
        da_copy = DynamicArray()
        for i in range(da.length()):
            da_copy.append(da[i])

        # get the last index of the da var: node_index
        last_node_index = da_copy.length() - 1

        # find its parent's index var: parent_index - (node_index - 1) // 2
        parent_index = (last_node_index - 1) // 2

        # loop
        while parent_index >= 0:
            # get children indices
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            # check if either child is less than parent, if so swap
            # first check if da[parent_index] is less than both children
            # if so, decrement parent_index and continue loop
            if left_child_index > da_copy.length() - 1 and right_child_index > da_copy.length() - 1:
                parent_index -= 1

            # choose left child if only left child has a value
            elif left_child_index <= da_copy.length() - 1 < right_child_index:
                if da_copy[parent_index] > da_copy[left_child_index]:
                    temp = da_copy[parent_index]
                    da_copy[parent_index] = da_copy[left_child_index]
                    da_copy[left_child_index] = temp
                    _percolate_down(da_copy, left_child_index)
                parent_index -= 1

            # choose right child if only right child has a value
            elif right_child_index <= da_copy.length() - 1 < left_child_index:
                if da_copy[parent_index] > da_copy[right_child_index]:
                    temp = da_copy[parent_index]
                    da_copy[parent_index] = da_copy[right_child_index]
                    da_copy[right_child_index] = temp
                    _percolate_down(da_copy, right_child_index)
                parent_index -= 1

            # if equal and less than, swap with left child
            elif left_child_index <= da_copy.length() - 1 and right_child_index <= da_copy.length() - 1:
                min_child_index = left_child_index if da_copy[left_child_index] <= da_copy[
                    right_child_index] else right_child_index
                if da_copy[parent_index] > da_copy[min_child_index]:
                    temp = da_copy[parent_index]
                    da_copy[parent_index] = da_copy[min_child_index]
                    da_copy[min_child_index] = temp
                    _percolate_down(da_copy, min_child_index)
                parent_index -= 1

            elif da_copy[parent_index] < da_copy[left_child_index] and da_copy[parent_index] < da_copy[
                right_child_index]:
                parent_index -= 1

            else:
                break

        # assign da as underlying array
        self._heap = da_copy
        return

        # clear contents of old da and make a copy
        # self.clear()
        # da = DynamicArray()
        # for i in range(da.length()):
        #     da.append(da[i])
        #
        # # get the last index of the da var: node_index
        # node_index = da.length() - 1
        #
        # # find its parent's index var: parent_index - (node_index - 1) // 2
        # parent_index = (node_index - 1) // 2
        #
        # # loop
        # while parent_index >= 0:
        #     # get children indices
        #     left_child_index = 2 * parent_index + 1
        #     right_child_index = 2 * parent_index + 2
        #
        #     # check if either child is less than parent, if so swap
        #     # first check if da[parent_index] is less than both children
        #     # if so, decrement parent_index and continue loop
        #     if da[parent_index] < da[left_child_index] and da[parent_index] < da[right_child_index]:
        #         parent_index -= 1
        #
        #     # choose left child if only left child has a value
        #     elif left_child_index <= da.length() - 1 < right_child_index:
        #         if da[parent_index] > da[left_child_index]:
        #             temp = da[parent_index]
        #             da[parent_index] = da[left_child_index]
        #             da[left_child_index] = temp
        #             _percolate_down(da, da[left_child_index])
        #             parent_index -= 1
        #
        #     # choose right child if only right child has a value
        #     elif right_child_index <= da.length() - 1 < left_child_index:
        #         if da[parent_index] > da[right_child_index]:
        #             temp = da[parent_index]
        #             da[parent_index] = da[right_child_index]
        #             da[right_child_index] = temp
        #             _percolate_down(da, da[right_child_index])
        #             parent_index -= 1
        #
        #     # if equal and less than, swap with left child
        #     elif left_child_index <= da.length() - 1 and right_child_index <= da.length() - 1:
        #         min_child_index = left_child_index if da[left_child_index] <= da[
        #             right_child_index] else right_child_index
        #         temp = da[parent_index]
        #         da[parent_index] = da[min_child_index]
        #         da[min_child_index] = temp
        #         _percolate_down(da, da[min_child_index])
        #         parent_index -= 1
        #
        # # assign da as underlying array
        # self._heap = da
        # return

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap.
        The runtime complexity of this implementation must be O(1).
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap.
        The runtime complexity of this implementation must be O(1).
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Receives a DynamicArray and sorts its content in non-ascending order,
    using the Heapsort algorithm. You must sort the array in place, without creating any data
    structures. This function does not return anything.
    You may assume that the input array will contain at least one element, and that values
    stored in the array are all of the same type (either all numbers, or strings, or custom
    objects, but never a mix of these). You do not need to write checks for these conditions.
    The runtime complexity of this implementation must be O(N log N). If the sort uses an
    algorithm other than Heapsort, you will not receive any points for this portion of the
    assignment, even if your function passes Gradescope.
    """
    # validation will have at least 1 element as per specs
    if da.length() == 1:
        return

    # build heap using BuildHeap code from MinHeap class
    # get the last index of the da var: node_index
    last_node_index = da.length() - 1

    # find its parent's index var: parent_index - (node_index - 1) // 2
    parent_index = (last_node_index - 1) // 2

    # loop
    while parent_index >= 0:
        # get children indices
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        # check if either child is less than parent, if so swap
        # first check if da[parent_index] is less than both children
        # if so, decrement parent_index and continue loop
        if left_child_index > da.length() - 1 and right_child_index > da.length() - 1:
            parent_index -= 1

        # choose left child if only left child has a value
        elif left_child_index <= da.length() - 1 < right_child_index:
            if da[parent_index] > da[left_child_index]:
                temp = da[parent_index]
                da[parent_index] = da[left_child_index]
                da[left_child_index] = temp
                _percolate_down(da, left_child_index)
            parent_index -= 1

        # choose right child if only right child has a value
        elif right_child_index <= da.length() - 1 < left_child_index:
            if da[parent_index] > da[right_child_index]:
                temp = da[parent_index]
                da[parent_index] = da[right_child_index]
                da[right_child_index] = temp
                _percolate_down(da, right_child_index)
            parent_index -= 1

        # if equal and less than, swap with left child
        elif left_child_index <= da.length() - 1 and right_child_index <= da.length() - 1:
            min_child_index = left_child_index if da[left_child_index] <= da[
                right_child_index] else right_child_index
            if da[parent_index] > da[min_child_index]:
                temp = da[parent_index]
                da[parent_index] = da[min_child_index]
                da[min_child_index] = temp
                _percolate_down(da, min_child_index)
            parent_index -= 1

        elif da[parent_index] < da[left_child_index] and da[parent_index] < da[right_child_index]:
            parent_index -= 1

        else:
            break
    # print da array to check if heap is built
    print(da)
    # get da first and last indexes
    first_index = 0

    # create a counting variable count_index and assign it the length of the da
    count_index = da.length() - 1

    dec_count = 0
    # loop condition: while count_index > 0
    while count_index > 0:
        # loop swapping count_index with first element
        first = da[first_index]
        da[first_index] = da[count_index]
        da[count_index] = first
        # decrement count_index by 1 each iteration through loop
        # if count_index == 0:
        #     break
        count_index -= 1
        # da_slice = da.slice(0, count_index + 1)
        # then percolating down to a slice of the da: da[:count_index]
        da.decrement_size()
        dec_count += 1
        _percolate_down(da, first_index)
    da.change_size(dec_count)


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Receives a DynamicArray and a parent node value and percolates the node down to its correct location in the MinHeap
    """
    # find node's index within da with validation
    node = da[parent]
    node_index = parent
    if node is None:
        return

    # loop until node is less than both children
    while True:
        # define variables for left and right children
        left_child_index = 2 * node_index + 1
        right_child_index = 2 * node_index + 2
        # break if left and right children are beyond the last element of the da
        if left_child_index > da.length() - 1 and right_child_index > da.length() - 1:
            break

        # choose left child if only left child has a value
        if left_child_index <= da.length() - 1 < right_child_index:
            if da[node_index] > da[left_child_index]:
                temp = da[node_index]
                da[node_index] = da[left_child_index]
                da[left_child_index] = temp
                node_index = left_child_index
            else:
                break

        # choose right child if only right child has a value
        elif right_child_index <= da.length() - 1 < left_child_index:
            if da[node_index] > da[right_child_index]:
                temp = da[node_index]
                da[node_index] = da[right_child_index]
                da[right_child_index] = temp
                node_index = right_child_index
            else:
                break

        # find min child and swap indexes (positions in the da)
        elif left_child_index <= da.length() - 1 and right_child_index <= da.length() - 1:
            # break if node is in the correct location; less than both children
            if da[node_index] < da[left_child_index] and da[node_index] < da[right_child_index]:
                break

            # if both sides are equal, min child will be the left child
            if da[left_child_index] == da[right_child_index]:
                min_child_index = left_child_index

            # min child will be the least of the two children
            else:
                min_child_index = left_child_index if da[left_child_index] < da[
                    right_child_index] else right_child_index

            if da[node_index] > da[min_child_index]:
                temp = da[node_index]
                da[node_index] = da[min_child_index]
                da[min_child_index] = temp
                node_index = min_child_index
            else:
                break

        else:
            break

    return

    # # find node's index within da with validation
    # node = None
    # node_index = None
    # for i in range(da.length()):
    #     if parent == da[i]:
    #         node = da[i]
    #         node_index = i
    #         break
    # if node is None:
    #     return
    #
    # # loop until node is less than both children
    # while True:
    #     # define variables for left and right children
    #     left_child_index = 2 * node_index + 1
    #     right_child_index = 2 * node_index + 2
    #     # break if left and right children are beyond the last element of the da
    #     if left_child_index > da.length() - 1 and right_child_index > da.length() - 1:
    #         break
    #
    #     # choose left child if only left child has a value
    #     if left_child_index <= da.length() - 1 < right_child_index:
    #         if da[node_index] > da[left_child_index]:
    #             temp = da[node_index]
    #             da[node_index] = da[left_child_index]
    #             da[left_child_index] = temp
    #             node_index = left_child_index
    #         else:
    #             break
    #
    #     # choose right child if only right child has a value
    #     elif right_child_index <= da.length() - 1 < left_child_index:
    #         if da[node_index] > da[right_child_index]:
    #             temp = da[node_index]
    #             da[node_index] = da[right_child_index]
    #             da[right_child_index] = temp
    #             node_index = right_child_index
    #         else:
    #             break
    #
    #     # find min child and swap indexes (positions in the da)
    #     elif left_child_index <= da.length() - 1 and right_child_index <= da.length() - 1:
    #         # break if node is in the correct location; less than both children
    #         if da[node_index] < da[left_child_index] and da[node_index] < da[right_child_index]:
    #             break
    #
    #         # if both sides are equal, min child will be the left child
    #         if da[left_child_index] == da[right_child_index]:
    #             min_child_index = left_child_index
    #
    #         # min child will be the least of the two children
    #         else:
    #             min_child_index = left_child_index if da[left_child_index] < da[
    #                 right_child_index] else right_child_index
    #
    #         if da[node_index] > da[min_child_index]:
    #             temp = da[node_index]
    #             da[node_index] = da[min_child_index]
    #             da[min_child_index] = temp
    #             node_index = min_child_index
    #         else:
    #             break
    #
    #     else:
    #         break
    #
    # return


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
