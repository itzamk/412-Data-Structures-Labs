import array

class Vector:
    def __init__(self):

        # Initialize an empty array with type 'd' (double precision floats)
        self._data = array.array('d', [])

        # Initialize the size to 0
        self._size = 0

        # Set the initial capacity to 2
        self._capacity = 2

        # Extend the array to the initial capacity with default values
        self._data.extend([0.0, 0.0])

    # Return the number of items in the vector
    def length(self):
        return self._size
    
    # Check if the item is contained in the vector
    def contains(self, item):
        return item in self._data

    # Return the item at the given index
    def getitem(self, ndx):

        # If index is valid, return item
        if 0 <= ndx < self._size:
            return self._data[ndx]
        
        # Print error
        else:
            print("Index out of range")

    # Set the item at the given index
    def setitem(self, ndx, item):
        
        # If index is valid
        if 0 <= ndx <= self._size:
            
            # If past the last item, append
            if ndx == self._size:  
                self.append(item)

            # Set if index is valid
            else:
                self._data[ndx] = item

        # Print error        
        else:
            print("Index out of range")
        
    # Append an item to the end of the vector
    def append(self, item):
        
        # Resize the array if the capacity is reached
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Add at end 
        self._data[self._size] = item

        # Increase size by 1
        self._size += 1

    # Insert an item at the given index
    def insert(self, ndx, item):
        
        # Resize the array if the capacity is reached
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Shift items to the right, make room
        for i in range(self._size, ndx, -1):
            self._data[i] = self._data[i - 1]

        # Insert at index
        self._data[ndx] = item

        # Increase size by 1
        self._size += 1

    # Remove and return the item at the given index
    def remove(self, ndx):
        
        # If valid index
        if 0 <= ndx < self._size:

            # Store value to be returned
            removed_item = self._data[ndx]

            # Shift items left, fill gap
            for i in range(ndx, self._size - 1):
                self._data[i] = self._data[i + 1]

            # Decrease size by 1
            self._size -= 1
            
            # Return item
            return removed_item
        
        # Print error
        else:
            print("Index out of range")

    # Return the index of the first occurrence of the item
    def indexOf(self, item):
        
        # Loop until item is found
        for i in range(self._size):

            # If found, return index
            if self._data[i] == item:
                return i
        
        # Print if not found
        print("Item not found in the vector")

    # Append the entire contents of another vector to this vector
    def extend(self, otherVector):
        
        # Loop through second vector
        for i in range(otherVector.length()):

            # Append each element to first vector
            self.append(otherVector.getitem(i))

    # Return a new vector that contains a subsequence of items
    def subVector(self, from_ndx, to_ndx):
        
        # If valid indices
        if 0 <= from_ndx <= to_ndx < self._size:

            # Create new vector (subvector)
            new_vector = Vector()

            # Loop through elements between 2 indices
            for i in range(from_ndx, to_ndx + 1):

                # Add elements to new subvector
                new_vector.append(self._data[i])

            # Return the subvector
            return new_vector
        
        # Print error
        else:
            ("Index out of range")

    # Resize the array to a new capacity
    def resize(self, new_capacity):

        # Create and initialize new array with new capacity
        new_data = array.array('d', [0.0] * new_capacity)

        # Loop through current array
        for i in range(self._size):

            # Add elements from current array to new
            new_data[i] = self._data[i]

        # Copy new data to current array
        self._data = new_data

        # Set new capacity
        self._capacity = new_capacity

# Example usage:
v = Vector()
v.append(1.0)
v.append(2.0)
v.setitem(2, 3.0)
print(v.getitem(0))  # 1.0
print(v.getitem(1))  # 2.0
print(v.getitem(2))  # 3.0
