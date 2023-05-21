# Name: Eusebius Ballentine
# OSU Email: ballente@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 05-22-2023
# Description: Binary Search Tree


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new value to the tree. Duplicate values are allowed. If a node with
        that value is already in the tree, the new value should be added to the right
        subtree of that node. It must be implemented with O(N) runtime complexity.
        """
        new_node = BSTNode(value)
        if self._root is None:
            self._root = new_node
            return

        prev = None
        curr = self._root
        flag = None
        while curr:
            # value is less than curr.value, move to curr.left
            if value < curr.value:
                prev = curr
                curr = prev.left
                flag = 'left'
            # value is greater than curr.value
            elif value > curr.value or (curr.value == value and curr.right is not None):
                prev = curr
                curr = prev.right
                flag = 'right'
            # value equals current node's value, add to node.right but consider conditions
            elif curr.value == value and curr.right is None:
                curr.right = new_node
                return

        # once we have reached a leaf node
        if flag == 'left':
            prev.left = new_node
        else:
            prev.right = new_node

    def remove(self, value: object) -> bool:
        """
        Removes a value from the tree. The method returns True if the value is
        removed. Otherwise, it returns False. It must be implemented with O(N) runtime
        complexity.

        When removing a node with two subtrees, replace it with the leftmost child
        of the right subtree (i.e. the inorder successor). You do not need to recursively
        continue this process. If the deleted node only has one subtree (either right or left),
        replace the deleted node with the root node of that subtree.
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
            # if node has one left child, replace it with its child's subtree
            elif curr.value == value and (curr.left and curr.right is None):
                if flag == 'left':
                    prev.left = curr.left
                elif flag == 'right':
                    prev.right = curr.left
                else:  # flag equals 'root'
                    self._root = curr.left
                return True
            # if node has one right child, replace it with its child's subtree
            elif curr.value == value and (curr.right and curr.left is None):
                if flag == 'left':
                    prev.left = curr.right
                elif flag == 'right':
                    prev.right = curr.right
                else:
                    self._root = curr.right
                return True
            # if node has no children
            elif curr.value == value and (curr.right is None and curr.left is None):
                if flag == 'left':
                    prev.left = curr.right
                elif flag == 'right':
                    prev.right = curr.right
                else:
                    self._root = curr.right
                return True

            # if node has two children, replace it with its inorder successor AND WE MUST CONTINUE DOWN THE TREE
            elif curr.value == value and (curr.left and curr.right):

                if curr.right.left is None:
                    replacement_node = curr.right
                    if curr == self._root:
                        replacement_node = curr.right
                        replacement_node.left = curr.left
                        curr.right = None
                        curr.left = None
                        self._root = replacement_node
                        return True

                    elif flag == 'left':
                        replacement_node = curr.right
                        prev.left = replacement_node
                        replacement_node.left = curr.left
                        return True

                    elif flag == 'right':
                        replacement_node = curr.right
                        prev.right = replacement_node
                        replacement_node.left = curr.left
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
            if inorder_successor.right:
                parent_successor.left = inorder_successor.right
            else:
                parent_successor.left = None
            inorder_successor.right = node_remove.right
            inorder_successor.left = node_remove.left
            node_remove.left = None
            node_remove.right = None


            # check which side we moved and assign the parent node of the removed node to the inorder succcessor
            if flag_remove == 'right':
                parent_remove.right = inorder_successor

            elif flag_remove == 'left':
                parent_remove.left = inorder_successor

            if node_remove == self._root:
                self._root = inorder_successor
            return True
        return False

    # Consider implementing methods that handle different removal scenarios; #
    # you may find that you're able to use some of them in the AVL.          #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Remove node that has no subtrees (no left or right nodes)
        """
        pass

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Remove node that has a left or right subtree (only)
        """
        pass

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Remove node that has two subtrees
        Need to find inorder successor and its parent (make a method!)
        """
        pass

    def contains(self, value: object) -> bool:
        """
        Returns True if the value is in the tree. Otherwise, it returns False. If the tree is
        empty, the method should return False. It must be implemented with O(N) runtime
        complexity.
        """
        if self._root is None:
            return False

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
                return True
        return False

    def inorder_traversal(self) -> Queue:
        """
        Perform an inorder traversal of the tree and return a Queue object that
        contains the values of the visited nodes, in the order they were visited. If the tree is empty,
        the method returns an empty Queue. It must be implemented with O(N) runtime
        complexity.
        """
        inorder_queue = Queue()
        if self._root is None:
            return inorder_queue

        prev = None
        curr = self._root
        while curr:






        pass

    def find_min(self) -> object:
        """
        Returns the lowest value in the tree. If the tree is empty, the method should
        return None. It must be implemented with O(N) runtime complexity.
        """
        if self._root is None:
            return None
        prev = None
        curr = self._root
        while curr:
            prev = curr
            curr = curr.left
        return prev.value

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
        return prev.value

    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty. Otherwise, it returns False. It must be
        implemented with O(1) runtime complexity.
        """
        if self._root is None:
            return True
        return False

    def make_empty(self) -> None:
        """
        TODO: Write your implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
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
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

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

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
