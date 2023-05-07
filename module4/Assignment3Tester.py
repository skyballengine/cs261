import unittest

from module4.queue_sll import Queue
from sll import *
from stack_sll import Stack

class Assignment3Tester(unittest.TestCase):

    # Singly Linked List Test Methods
    def test_inspect(self):
        lst = LinkedList()
        print(lst)

    def test_insert_front(self):
        test_case = ["A", "B", "C"]
        lst = LinkedList()
        for case in test_case:
            lst.insert_front(case)
            print(lst)

    def test_insert_back(self):
        test_case = ["C", "B", "A"]
        lst = LinkedList()
        for case in test_case:
            lst.insert_back(case)
            print(lst)

    def test_insert_at_index(self):
        lst = LinkedList()
        test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
        for index, value in test_cases:
            print("Inserted", value, "at index", index, ": ", end="")
            try:
                # print(lst.length())
                lst.insert_at_index(index, value)
                print(lst)
            except Exception as e:
                print(type(e))

    def test_remove_from_index(self):
        lst = LinkedList([1, 2, 3, 4, 5, 6])
        print(f"Initial LinkedList : {lst}")
        for index in [0, 2, 0, 2, 2, -2]:
            print("Removed at index:", index, ": ", end="")
            try:
                lst.remove_at_index(index)
                print(lst)
            except Exception as e:
                print(type(e))
        print(lst)

    def test_remove(self):
        # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
        # print(f'Initial LinkedList, Length: {lst.length()}\n {lst}')
        # for value in [7, 3, 3, 3, 3]:
        #     print(f'remove({value}): {lst.remove(value)}, Length: {lst.length()}')
        #     f' \n {lst}'
        lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
        print(f'Initial LinkedList, Length: {lst.length()}\n {lst}')
        for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
            print(f'remove({value}): {lst.remove(value)}, Length: {lst.length()}')
            print(f' \n {lst}')
    def test_count(self):
        lst = LinkedList([1, 2, 3, 1, 2, 2])
        print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    def test_find(self):
        lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
        print(lst)
        print(lst.find("Waldo"))
        print(lst.find("Superman"))
        print(lst.find("Santa Claus"))

    def test_slice(self):
        # lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # ll_slice = lst.slice(1, 3)
        # print("Source:", lst)
        # print("Start: 1 Size: 3 :", ll_slice)
        # ll_slice.remove_at_index(0)
        # print("Removed at index 0 :", ll_slice)
        lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
        print("Source:", lst)
        slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
        for index, size in slices:
            print("Start:", index, "Size:", size, end="")
            try:
                print(" :", lst.slice(index, size))
            except:
                print(" : exception occurred.")

    # Stack Dynamic Array

    def test_da_push(self):
        pass

    def da_pop(self):
        pass

    def test_da_top(self):
        pass

    # Stack List Nodes

    def test_ln_push(self):
        s = Stack()
        print(s)
        for value in [1, 2, 3, 4, 5]:
            s.push(value)
        print(s)

    def test_ln_pop(self):
        s = Stack()
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))
        for value in [1, 2, 3, 4, 5]:
            s.push(value)
        for i in range(6):
            try:
                print(s.pop())
            except Exception as e:
                print("Exception:", type(e))

    def test_ln_top(self):
        s = Stack()
        try:
            s.top()
        except Exception as e:
            print("No elements in stack", type(e))
        s.push(10)
        s.push(20)
        print(s)
        print(s.top())
        print(s.top())
        print(s)

    # Queue Dynamic Array

    def test_da_enqueue(self):
        pass

    def test_da_dequeue(self):
        pass

    def test_da_front(self):
        pass

    # Queue List Nodes
    def test_ln_enqueue(self):
        q = Queue()
        print(q)
        for value in [1, 2, 3, 4, 5]:
            q.enqueue(value)
        print(q)

    def test_ln_dequeue(self):
        pass

    def test_ln_front(self):
        pass
