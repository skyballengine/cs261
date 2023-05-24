# Name: Eusebius Ballentine
# OSU Email: ballente@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 05-22-2023
# Description: AVL Tree


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new value to the tree while maintaining its AVL property. Duplicate
        values are not allowed. If the value is already in the tree, the method should not change
        the tree. It must be implemented with O(log N) runtime complexity.
        """
        #     curr = self._root
        #     self.add_util(curr, value)
        #     return curr
        #
        # def add_util(self, root=None, value=None):
        #     if not root:
        #         return AVLNode(value)
        #
        #     elif value < root.value:
        #         root.left = self.add_util(root.left, value)
        #     else:
        #         root.right = self.add_util(root.right, value)
        #
        #     root.height = self._get_height(root.right) - self._get_height(root.left)
        new_node = AVLNode(value)
        prev = None
        curr = self._root
        flag = None

        if self._root is None:
            self._root = new_node
            return

        while curr:
            # value is less than curr.value, move to curr.left
            if value < curr.value:
                prev = curr
                curr = prev.left
                flag = 'left'

            # value is greater than curr.value
            elif value > curr.value:
                prev = curr
                curr = prev.right
                flag = 'right'

            # value equals current node's value break and do nothing for AVL Trees
            else:
                return

        # once we have reached a leaf node
        if flag == 'left':
            prev.left = new_node
            new_node.parent = prev

        else:
            prev.right = new_node
            new_node.parent = prev

        curr = new_node
        parent_node = curr.parent
        while parent_node is not None:
            self._rebalance(parent_node)
            parent_node = parent_node.parent

    def remove(self, value: object) -> bool:
        """
        Removes the value from the AVL tree. The method returns True if the value is
        removed. Otherwise, it returns False. It must be implemented with O(log N) runtime
        complexity.
        NOTE: See ‘Specific Instructions’ for an explanation of which node replaces the deleted
        node.
        """
        if self._root is None:
            return False

        flag_remove = None
        parent_remove = None
        node_remove = None
        need_successor = None
        flag = 'root'
        prev = None
        curr = self._root
        while curr:
            # go left
            if value < curr.value or need_successor:  # include condition in case we need to continue left
                # if we have established we need the inorder successor
                if need_successor:
                    if curr.left is None:
                        # now we know the parent and the inorder successor
                        parent_successor = prev
                        # prev will be the inorder successor
                        prev = curr
                        break

                    else:  # there is a left child of the right child
                        # keep going left, tracking 3 nodes
                        parent_successor = prev
                        prev = curr  # prev will be the inorder successor
                        curr = curr.left

                else:
                    prev = curr
                    curr = prev.left
                    flag = 'left'
            # go right
            elif value > curr.value:
                prev = curr
                curr = prev.right
                flag = 'right'

            # if curr.value equals value, we have found the node
            # if node only has one left child, replace node with its left subtree
            elif curr.value == value and (curr.left and curr.right is None):
                if flag == 'left':
                    prev.left = curr.left
                    # assign parent_remove for rebalancing
                    parent_remove = prev
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent

                elif flag == 'right':
                    prev.right = curr.left
                    # assign parent_remove for rebalancing
                    parent_remove = prev
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent

                else:  # flag equals 'root'
                    self._root = curr.left
                return True
            # if node has one right child, replace node with its right subtree
            elif curr.value == value and (curr.right and curr.left is None):
                if flag == 'left':
                    prev.left = curr.right
                    # assign parent_remove for rebalancing
                    parent_remove = prev
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent

                elif flag == 'right':
                    prev.right = curr.right
                    # assign parent_remove for rebalancing
                    parent_remove = prev
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent

                else:
                    self._root = curr.right
                    parent_remove = curr.parent
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent
                return True
            # if node has no children
            elif curr.value == value and (curr.right is None and curr.left is None):
                if flag == 'left':
                    prev.left = curr.right
                    # assign parent_remove for rebalancing
                    parent_remove = prev
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent

                elif flag == 'right':
                    prev.right = curr.right
                    # assign parent_remove for rebalancing
                    parent_remove = prev
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent

                else:
                    self._root = curr.right
                    parent_remove = curr.parent
                    while parent_remove is not None:
                        self._rebalance(parent_remove)
                        parent_remove = parent_remove.parent
                return True

            # if node has two children, replace it with its inorder successor, start at node.right then CONTINUE LEFT DOWN THE TREE
            elif curr.value == value and (curr.left and curr.right):

                if curr.right.left is None:
                    if curr == self._root:
                        replacement_node = curr.right
                        # print(replacement_node)
                        replacement_node.left = curr.left
                        curr.right = None
                        curr.left = None
                        replacement_node.left.parent = replacement_node
                        self._root = replacement_node
                        replacement_node.parent = curr.parent
                        self._rebalance(replacement_node)
                        return True

                    elif flag == 'left':
                        replacement_node = curr.right
                        prev.left = replacement_node
                        replacement_node.left = curr.left
                        # assign parent_remove for rebalancing

                        # TODO parent_remove = curr.parent
                        replacement_node.parent = curr.parent
                        # curr.parent = None
                        # curr.right = None
                        # curr.left = None

                        parent_remove = replacement_node

                        while parent_remove is not None:
                            self._rebalance(parent_remove)
                            parent_remove = parent_remove.parent

                        return True

                    elif flag == 'right':
                        replacement_node = curr.right
                        prev.right = replacement_node
                        replacement_node.left = curr.left
                        # assign parent_remove for rebalancing

                        # TODO parent_remove = curr.parent
                        replacement_node.parent = curr.parent
                        # curr.parent = None
                        # curr.right = None
                        # curr.left = None

                        parent_remove = replacement_node
                        while parent_remove is not None:
                            self._rebalance(parent_remove)
                            parent_remove = parent_remove.parent
                        return True

                # if there is a curr.right.left, look for inorder successor
                need_successor = True
                parent_remove = prev
                node_remove = curr
                flag_remove = flag
                prev = curr.right
                curr = curr.right.left
                parent_successor = None

        if need_successor:
            inorder_successor = prev
            # if inorder successor has a right node, update its parent.left points to it
            if inorder_successor.right:
                parent_successor.left = inorder_successor.right
                inorder_successor.right.parent = parent_successor
                # parent_successor.parent = inorder_successor # check back?
            else:
                parent_successor.left = None
                # parent_successor.parent = inorder_successor  # check back

            # update inorder successor pointers - also the parent pointer
            inorder_successor.right = node_remove.right
            inorder_successor.left = node_remove.left
            inorder_successor.parent = node_remove.parent
            # check this
            if inorder_successor.left is not None:
                inorder_successor.left.parent = inorder_successor
            if inorder_successor.right is not None:
                inorder_successor.right.parent = inorder_successor

            # check which side we moved and assign the parent node of the removed node to the inorder succcessor
            # need to update parents?
            # if node to be removed is the root
            if node_remove == self._root:
                self._root = inorder_successor
                node_remove.right.parent = inorder_successor
                node_remove.left.parent = inorder_successor

            elif flag_remove == 'right':
                parent_remove.right = inorder_successor

            elif flag_remove == 'left':
                parent_remove.left = inorder_successor
                node_remove.left.parent = inorder_successor  # check back

            # update node_remove properties
            node_remove.left = None
            node_remove.right = None
            node_remove.parent = None  # TODO: Changed

            # assign parent_remove for rebalancing
            parent_remove = parent_successor  # TODO: CHANGED for rebalancing, but program crashes now
            while parent_remove is not None:
                self._rebalance(parent_remove)
                parent_remove = parent_remove.parent
            return True
        return False


    # It's highly recommended to implement                          #
    # the following methods for balancing the AVL Tree.             #
    # Remove these comments.                                        #
    # Remove these method stubs if you decide not to use them.      #
    # Change these methods in any way you'd like.                   #

    def _balance_factor(self, node: AVLNode) -> int:
        """
        Determine if subtree rooted at a node is height balanced
        Difference in height between right subtree and left subtree
        Balanced if -1, 1, or 0
        Note: NULL nodes have a height of -1, thus every leaf node will have a balance factor of 0
        ex: -1 - (-1) = 0
        """
        if not node:
            return 0

        return self._get_height(node.right) - self._get_height(node.left)

    def _get_height(self, node: AVLNode) -> int:
        """
        Determine height of a node's subtree
        """
        if not node:
            return -1

        return node.height

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Perform a left rotation at the given node
        """
        c = node.right
        node.right = c.left
        if node.right is not None:
            node.right.parent = node
        c.left = node
        node.parent = c
        self._update_height(node)
        self._update_height(c)
        return c

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Perform a right roatation at the given node
        """
        c = node.left
        node.left = c.right
        if node.left is not None:
            node.left.parent = node
        c.right = node
        node.parent = c
        self._update_height(node)
        self._update_height(c)
        return c

    def _update_height(self, node: AVLNode) -> None:
        """
        Update the height property of the given node
        """
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _rebalance(self, node: AVLNode) -> None:
        """
        Rebalance the subtrees of the given node
        """
        node_parent = node.parent
        if self._balance_factor(node) < - 1:
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
                node.left.parent = node
            new_subtree_root = self._rotate_right(node)
            new_subtree_root.parent = node_parent
            # node.parent.left or node.parent.right = new_subtree_root
            if node == self._root or node_parent is None:
                self._root = new_subtree_root
            elif node == node_parent.left:
                node_parent.left = new_subtree_root
            else:
                node_parent.right = new_subtree_root

        elif self._balance_factor(node) > 1:
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
                node.right.parent = node
            new_subtree_root = self._rotate_left(node)
            new_subtree_root.parent = node_parent
            # node.parent.left or node.parent.right = new_subtree_root
            if node == self._root or node_parent is None:
                self._root = new_subtree_root
            elif node == node_parent.left:
                node_parent.left = new_subtree_root
            else:
                node_parent.right = new_subtree_root

        else:
            self._update_height(node)

    # comment out or delete before submission
    def find_max(self) -> object:
        """
        Returns the highest value in the tree. If the tree is empty, the method should
        return None. It must be implemented with O(N) runtime complexity.
        """
        if self._root is None:
            return None
        prev = None
        curr = self._root
        while curr:
            prev = curr
            curr = curr.right
        return prev, prev.value

    # comment out or delete before submission
    def contains(self, value: object) -> AVLNode:
        """
        Returns True if the value is in the tree. Otherwise, it returns False. If the tree is
        empty, the method should return False. It must be implemented with O(N) runtime
        complexity.
        """
        if self._root is None:
            return

        curr = self._root

        while curr:
            # go left
            if value < curr.value:
                prev = curr
                curr = prev.left
            # go right
            elif value > curr.value:
                prev = curr
                curr = prev.right

            else:
                return curr
        return f'No node with {value}'


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
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

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
