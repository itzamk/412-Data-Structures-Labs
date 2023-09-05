class Array:
    def __init__(self, capacity=2):
        self._data = [None] * capacity
        self._capacity = capacity

    def __getitem__(self, ndx):
        return self._data[ndx]

    def __setitem__(self, ndx, value):
        self._data[ndx] = value

    def __len__(self):
        return self._capacity

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._capacity):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity


class Vector:
    def __init__(self):
        self._data = Array()
        self._size = 0

    def length(self):
        return self._size

    def contains(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return True
        return False

    def getitem(self, ndx):
        if ndx < 0 or ndx >= self._size:
            raise IndexError("Index out of range")
        return self._data[ndx]

    def setitem(self, ndx, item):
        if ndx < 0 or ndx > self._size:
            raise IndexError("Index out of range")
        if ndx == self._size:
            self.append(item)
        else:
            self._data[ndx] = item

    def append(self, item):
        if self._size == len(self._data):
            self._data.resize(2 * len(self._data))
        self._data[self._size] = item
        self._size += 1

    def insert(self, ndx, item):
        if ndx < 0 or ndx > self._size:
            raise IndexError("Index out of range")
        if self._size == len(self._data):
            self._data.resize(2 * len(self._data))
        for i in range(self._size, ndx, -1):
            self._data[i] = self._data[i - 1]
        self._data[ndx] = item
        self._size += 1

    def remove(self, ndx):
        if ndx < 0 or ndx >= self._size:
            raise IndexError("Index out of range")
        removed_item = self._data[ndx]
        for i in range(ndx, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        return removed_item

    def indexOf(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return i
        raise ValueError("Item not found in the list")

    def extend(self, otherVector):
        for i in range(otherVector.length()):
            self.append(otherVector.getitem(i))

    def subVector(self, from_ndx, to_ndx):
        if from_ndx < 0 or from_ndx >= self._size or to_ndx < 0 or to_ndx >= self._size:
            raise IndexError("Index out of range")
        new_vector = Vector()
        for i in range(from_ndx, to_ndx + 1):
            new_vector.append(self._data[i])
        return new_vector
