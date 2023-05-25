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
        # if heap is empty append node value to the da
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
        pass

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order, and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        The runtime complexity of this implementation must be O(N). If the runtime complexity is
        O(N log N), you will not receive any points for this portion of the assignment, even if your
        method passes Gradescope.
        """
        pass

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
    pass


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Receives a DynamicArray and a parent node value and percolates the node down to its correct location in the MinHeap
    """
    pass


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
