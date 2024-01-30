class Jar:
    def __init__(self, capacity=12,size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self.size > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size > self.capacity:
            raise ValueError("Size must be a non-negative integer.")
        self._size = size




jar = Jar(8,2)
jar.deposit(4)
jar.withdraw(6)
print(jar)
