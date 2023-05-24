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
        print("\nPDF - method add() example 1")
        print("----------------------------")
        #
        # tree = AVL()
        # tree.add(1)
        # tree.add(2)
        # tree.add(3)
        # print(tree)
        # print(tree.is_valid_avl())
        test_cases = (
            (1, 2, 3),  # RR
            (3, 2, 1),  # LL
            (1, 3, 2),  # RL
            (3, 1, 2),  # LR
        )
        for case in test_cases:
            tree = AVL(case)
            print(tree)
            print(tree.is_valid_avl())

        test_cases = (
            (10, 20, 30, 40, 50),  # RR, RR
            (10, 20, 30, 50, 40),  # RR, RL
            (30, 20, 10, 5, 1),  # LL, LL
            (30, 20, 10, 1, 5),  # LL, LR
            (5, 4, 6, 3, 7, 2, 8),  # LL, RR
            (range(0, 30, 3)),
            (range(0, 31, 3)),
            (range(0, 34, 3)),
            (range(10, -10, -2)),
            ('A', 'B', 'C', 'D', 'E'),
            (1, 1, 1, 1),
        )
        for case in test_cases:
            tree = AVL(case)
            print('INPUT  :', case)
            print('RESULT :', tree)

    def test_remove_avl(self):

        tree = AVL([0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])
        print(tree)
        print(tree.is_valid_avl())
        tree.remove(21)
        print(tree)
        print(tree.is_valid_avl())
        tree.remove(24)
        print(tree)
        print(tree.is_valid_avl())
        tree.remove(27)
        print(tree)
        print(tree.is_valid_avl())
        tree.remove(9)
        print(tree)
        print(tree.is_valid_avl())

        print(f'\nTest 5')
        for _ in range(100):
            case = list(set(random.randrange(1, 20000) for _ in range(900)))
            tree = AVL(case)
            for value in case[::2]:
                tree.remove(value)
            if not tree.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('Stress test finished')

    def test_remove_two_subtrees_avl(self):
        pass

    def test_balance_factor_avl(self):
        pass

    def test_get_height_avl(self):
        tree = AVL([10, 20, 5, 15, 17, 7, 12, 6])
        print(tree)
        print(tree.is_valid_avl())
        tree.add(25)
        print(tree)
        tree.add(50)
        print(tree)
        tree.add(40)
        print(tree)
        tree.add(45)
        print(tree)
        tree.add(42)
        print(tree)
        tree.add(19)
        print(tree)
        tree.add(18)
        print(tree)
        node = tree.contains(12)
        print(node.height)
        print(tree.contains(1000))
        # print('First run')
        # for num in [50, 40, 45, 42, 6, 19, 18]:
        #     node = tree.contains(num)
        #     print(f'Node {num} height: {node.height}')
        #
        # print('\nSecond run')
        # for num in [10, 7, 25, 12, 20, 15]:
        #     node = tree.contains(num)
        #     node_height = tree._get_height(node)
        #     print(f'Node {num} height: {node_height}')


    def test_rotate_left_avl(self):
        pass

    def test_rotate_right_avl(self):
        pass

    def test_update_height_avl(self):
        pass

    def test_rebalance_avl(self):
        pass