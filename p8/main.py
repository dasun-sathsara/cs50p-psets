class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        print(f'(name="{self.name}" , age={self.age} , salary={self.salary})')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        assert name, "name can't be empty"
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        assert age is int, "age should be an integer"
