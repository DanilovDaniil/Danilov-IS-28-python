# Создание базового класса "Животное" и его наследование для создания классов
# "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
# и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
# такие как "гавкать" и "мурлыкать".

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def breathe(self):
        print(f"{self.name} дышит...")

    def eat(self, food):
        print(f"{self.name} ест {food}")

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, возраст: {self.age}"


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def purr(self):
        print(f"{self.name} мурлычет: Мррр...")


if __name__ == "__main__":
    dog = Dog("Бобик", 3)
    cat = Cat("Мурка", 2)

    print(dog)
    print(cat)

    dog.breathe()
    dog.bark()

    cat.eat("рыбу")
    cat.purr()
