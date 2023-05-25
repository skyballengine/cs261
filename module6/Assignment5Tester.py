import unittest
from min_heap import *

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
        pass

    def test_build_heap(self):
        pass

    def test_size(self):
        pass

    def test_clear(self):
        pass

    def test_heap_sort(self):
        pass

    def test_percolate_down(self):
        pass

