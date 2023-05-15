from static_array import StaticArray

class DynamicArrayException(Exception):

    """

    Custom exception class to be used by Dynamic Array

    DO NOT CHANGE THIS CLASS IN ANY WAY

    """

    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def dynArrayAddAt(self, index: int, value: object) -> None:
        """
        Write this implementation
        """
        if index < 0 or index > self.size - 1:
            raise DynamicArrayException

        if self.size == self.capacity:
            new_sa = StaticArray(self.capacity * 2)

            for i in range(index, self.size):
                new_sa[i + 1] = self.data[i]

            for i in range(0, index):
                new_sa[i] = self.data[i]
            new_sa[index] = value
            self.size += 1

        else:
            for i in range(self.size, index, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = value
            self.size += 1

        return
