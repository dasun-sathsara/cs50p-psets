
class Jar:
    COOKIE = "🍪"

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return Jar.COOKIE * self.size

    def deposit(self, amount: int):
        if not (amount + self.size > self.capacity):
            self.size += amount
        else:
            raise ValueError("not enough space in the jar")

    def withdraw(self, amount: int):
        if not(amount > self.size):
            self.size -= amount
        else:
            raise ValueError("don't have that many cookies")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            assert type(capacity) == int and capacity > 0
            self._capacity = capacity
        except AssertionError:
            raise ValueError("invalid value for capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, amount):
        try:
            assert type(amount) == int and amount > 0
            self._size = amount
        except AssertionError:
            raise ValueError("invalid value for size")


jar = Jar(15)
jar.deposit(5)
jar.withdraw(3)
print(jar.size)
print(jar.capacity)
jar.deposit(10)
jar.withdraw(1)
print(jar.size)
print(jar)
