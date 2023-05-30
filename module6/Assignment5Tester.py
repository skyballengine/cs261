import unittest
from min_heap import *
from min_heap import _percolate_down

class Assignment5Test(unittest.TestCase):

    def test_add(self):
        h = MinHeap()
        print(h, h.is_empty())
        for value in ['bird', 'fish', 'monkey', 'zebra']:
            h.add(value)
            print(h)
        h.add('elephant')
        print(h)

        h = MinHeap([300])
        h.add(285)
        print(h)


    def test_is_empty(self):
        pass

    def test_get_min(self):
        pass

    def test_remove_min(self):
        print("\nPDF - remove_min example 1")
        print("--------------------------")
        h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
        while not h.is_empty() and h.is_empty() is not None:
            print(h, end=' ')
            print(h.remove_min())
        print(h)
        # print(h.remove_min())

        print("\nPDF - remove_min example 2")
        print("--------------------------")
        h = MinHeap(['_aunE^d', 'aUp', 'aUp', 't_IJE]GN_', 'j^tjQ', 'tdhwv'])
        while not h.is_empty() and h.is_empty() is not None:
            print(h, end=' ')
            print(h.remove_min())
        print(h)

    def test_build_heap(self):
        print("\nPDF - build_heap example 1")
        print("--------------------------")
        # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
        # h = MinHeap(['zebra', 'apple'])
        # print(h)
        # h.build_heap(da)
        # print(h)
        #
        # print("--------------------------")
        # print("Inserting 500 into input DA:")
        # da[0] = 500
        # print(da)
        #
        # print("Your MinHeap:")
        # print(h)
        # if h.get_min() == 500:
        #     print("Error: input array and heap's underlying DA reference same object in memory")
        # da = DynamicArray([-11417, -11417, -49446, 34031, 29065, -55793, -43165, -65767, -49314])
        # h = MinHeap([-48266, -6559, 7387, 11466, 20380, 20380, 12651, 90405, 80907, 27022])
        # print(h)
        # h.build_heap(da)
        # print(h)
        # print(f'Should be: [-65767, -49314, -55793, -11417, 29065, -49446, -43165, 34031, -11417]')

        da = DynamicArray([-898, -89811, 53788, 73451, -53933, -8124, 89798, -69430, 16625, 16625])
        h = MinHeap([-84311, -2837, -34256, 4278, -2837, 70724, -12627])
        print(h)
        h.build_heap(da)
        print(h)
        print(f'Should be: [-89811, -69430, -8124, -898, -53933, 53788, 89798, 73451, 16625, 16625]')



    def test_size(self):
        pass

    def test_clear(self):
        pass

    def test_heap_sort(self):
        # print("\nPDF - heapsort example 1")
        # print("------------------------")
        # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
        # print(f"Before: {da}")
        # heapsort(da)
        # print(f"After:  {da}")

        # print("\nPDF - heapsort example 2")
        # print("------------------------")
        # da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
        # print(f"Before: {da}")
        # heapsort(da)
        # print(f"After:  {da}")

    def test_percolate_down(self):
        h = MinHeap([2, 5, 3, 8, 6])
        print(h)
        print(_percolate_down(h._heap, 15))

    # dynamic_array tests

    def test_pop(self):
        da = DynamicArray([1, 2, 3, 4, 5])
        print(da)
        da.pop()
        print(da)

    def test_decrement_size(self):
        da = DynamicArray([1, 2, 3, 4, 5])
        print(da)
        da.decrement_size()
        print(da)

