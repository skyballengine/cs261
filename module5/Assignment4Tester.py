import unittest
from bst import *
from avl import *
class Assignment4Tester(unittest.TestCase):

    # testing for BST objects
    def test_add(self):
        # test 1
        print('Test 1')
        test_cases = (
            (1, 2, 3),
            (3, 2, 1),
            (1, 3, 2),
            (3, 1, 2)
        )
        for case in test_cases:
            tree = BST(case)
            print(tree)
            print(tree.is_valid_bst())

        # test 2
        print('\nTest 2')
        test_cases = (
            (10, 20, 30, 40, 50),
            (10, 20, 30, 50, 40),
            (30, 20, 10, 5, 1),
            (30, 20, 10, 1, 5),
            (5, 4, 6, 3, 7, 2, 8),
            (range(0, 30, 3)),
            (range(0, 31, 3)),
            (range(0, 34, 3)),
            (range(10, -10, -2)),
            ('A', 'B', 'C', 'D', 'E'),
            (1, 1, 1, 1),
        )
        for case in test_cases:
            tree = BST(case)
            print('INPUT :', case)
            print('RESULT :', tree)
            print(tree.is_valid_bst())

        # test 3
        print('\nTest 3')
        for _ in range(100):
            case = list(set(random.randrange(1, 20000) for _ in range(900)))
            tree = BST()
            for value in case:
                tree.add(value)
            if not tree.is_valid_bst():
                raise Exception("Problem with add operation")
        print('add() stress test finished')

        # test with random values
        case = [16, -15, -8, -7, 3, -19, -16, -3, 4, 18, 8, -19, -5, 11, 10, 1, -2, 19, -15, 17, 20, -17, 6, 12, -20, 11, -3, 4, 4, -19]
        tree = BST(case)
        print('INPUT :', case)
        print('RESULT :', tree)
        print(tree.is_valid_bst())
    def test_remove(self):
        # test 1
        print("\nPDF - method remove() example 1")
        print("-------------------------------")
        test_cases = (
            ((1, 2, 3), 1),
            ((1, 2, 3), 2),
            ((1, 2, 3), 3),
            ((50, 40, 60, 30, 70, 20, 80, 45), 0),
            ((50, 40, 60, 30, 70, 20, 80, 45), 45),
            ((50, 40, 60, 30, 70, 20, 80, 45), 40),
            ((50, 40, 60, 30, 70, 20, 80, 45), 30),
        )
        for case, del_value in test_cases:
            tree = BST(case)
            print('INPUT  :', tree, "DEL:", del_value)
            tree.remove(del_value)
            print('RESULT :', tree)

        tree = BST([-57, -86, 76, 77, 14, 46, -14, 28, -66, -97])
        print('INPUT  :', tree)
        tree.remove(-57)
        print('RESULT :', tree)

        tree = BST([-28, 38, 71, -17, 16, 82, -12, 22, 24, -100])
        print('INPUT  :', tree)
        tree.remove(-28)
        print('RESULT :', tree)

        tree = BST([-94, -84, -20, -51, -83, -16, -76, -42, -67, -34])
        print('INPUT  :', tree)
        tree.remove(-94)
        print('RESULT :', tree)
        tree.remove(-20)
        print('RESULT :', tree)

        tree = BST([96, -96, -32, 34, 100, 37, -89, -81, -12, -100])
        print('INPUT  :', tree)
        print(tree.remove(96))
        print('RESULT :', tree)

        tree = BST([66, 70, 41, 11, 12, -74, 23, 62, 61, 30])
        print('INPUT  :', tree)
        print(tree.remove(66))
        print('RESULT :', tree)
        print(tree.remove(41))
        print('RESULT :', tree)

        tree = BST([99, -23, -18, 48, 83, -12, 52, -13, 26, -100])
        print('INPUT  :', tree)
        print(tree.remove(99))
        print('RESULT :', tree)

        tree = BST([-31, 37, 7, 50, -10, 23, -39, -38, 92, 25])
        print('INPUT  :', tree)
        tree.remove(-31)
        print('RESULT :', tree)
        tree.remove(7)
        print('RESULT :', tree)
        tree.remove(-10)
        print('RESULT :', tree)

    def test_remove_no_subtrees(self):
        pass

    def test_remove_one_subtree(self):
        pass

    def test_remove_two_subtrees(self):
        pass

    def test_contains(self):
        pass

    def test_inorder_traversal(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        print(tree.inorder_traversal())

    def test_find_min(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        print(tree.find_min())

    def test_find_max(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        print(tree.find_max())

    def test_is_empty(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        print(tree._root)
        print(tree._root.left)
        print(tree.is_empty())
        tree1 = BST([])
        print(tree.is_empty())

    def test_make_empty(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        tree.make_empty()
        print(tree)

        tree = BST()
        tree.make_empty()
        print(tree)

    # testing for AVL objects

    def test_add_avl(self):
        pass

    def test_remove_avl(self):
        pass

    def test_remove_two_subtrees_avl(self):
        pass

    def test_balance_factor_avl(self):
        pass

    def test_get_height_avl(self):
        pass

    def test_rotate_left_avl(self):
        pass

    def test_rotate_right_avl(self):
        pass

    def test_update_height_avl(self):
        pass

    def test_rebalance_avl(self):
        pass