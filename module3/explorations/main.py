from static_array import StaticArray

class Dynamic_Array:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        """
        self.size = 0
        self.capacity = 10
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self):
        return str(self.data)

    # Will need to be amended to check if there is room and call function to expand array when necessary
    def append(self, val):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
            self.data[self.size] = val
            self.size = self.size + 1
        else:
            self.data[self.size] = val
            self.size = self.size + 1

    # Add a function that will create an expanded array with twice the size with the same elements
    def resize(self, new_capacity: int) -> None:
        """
        Double capacity of underlying static array when necessary
        """
        new_sa = StaticArray(new_capacity)
        for i in range(self.data.length()):
            new_sa[i] = self.data[i]
        self.data = new_sa

# Create new instance of Dynamic_Array
my_list = Dynamic_Array([3, 5, 4, 6])

# Build list with 10 items
for i in range(12):
  my_list.append(i)

# Output list
print(my_list)