# Name: Eusebius Ballentine
# OSU Email: ballente@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2b
# Due Date: May 1
# Description: Implement a Bag ADT


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag. It must be implemented with O(1) amortized
        runtime complexity.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the provided value
        object. It returns True if some object was actually removed from the bag. Otherwise, it
        returns False. This method must be implemented with O(N) runtime complexity.
        """
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Returns the number of elements in the bag that match the provided value
        object. It must be implemented with O(N) runtime complexity.
        """
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the contents of the bag. It must be implemented with O(1) runtime
        complexity.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares the contents of a bag with the contents of a second bag provided as
        a parameter. The method returns True if the bags are equal (contain the same number of
        elements, and also contain the same elements without regard to the order of elements).
        Otherwise, it returns False. An empty bag is only considered equal to another empty bag.
        This method must not change the contents of either bag. You are allowed to directly access
        all instance variables of second_bag, but you may not create any additional data structures,
        nor sort either bag. The runtime complexity of this implementation should be no greater
        than O(N2).
        """
        # if both bags empty, then equal
        if self._da.is_empty() and second_bag._da.is_empty():
            return True

        # if bags of different length, then NOT equal
        if self.size() != second_bag.size():
            return False

        # set flag to false initially
        flag = False
        for i in range(self.size()):
            in_arr = False
            for j in range(second_bag.size()):
                if self._da[i] == second_bag._da[j]:
                    if self.count(self._da[i]) == second_bag.count(second_bag._da[j]):
                        flag = True
                        in_arr = True
                        continue
                    else:
                        return False
            if not in_arr:
                return False
        return flag
        # nested loops to check if elements are in
        # for i in range(self._da.length()):
        #     flag = False
        #     count = 0
        #     for j in range(second_bag._da.length()):
        #         if self._da[i] == second_bag._da.get_at_index(j):
        #             count += 1
        #             flag = True
        #     if not flag:
        #         return False
        # return True

    def __iter__(self):
        """
        Enables the Bag to iterate across itself. Implement this method in a similar way
        to the example in the Exploration: Encapsulation and Iterators.
        You ARE permitted (and will need to) initialize a variable to track the iterator’s progress
        through the Bag’s contents.
        You can use either of the two models demonstrated in the Exploration - you can build the
        iterator functionality inside the Bag, or you can create a separate iterator class
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Return the next item in the Bag, based on the current location of the
        iterator.
        """
        try:
            value = self._da.get_at_index(self._index)

        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
