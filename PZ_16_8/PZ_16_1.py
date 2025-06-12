# Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
# который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
# Пол: пол".

class Human:
    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.sex}"


human1 = Human("Иван", 30, "мужской")
print(human1.info())

human2 = Human("Мария", 25, "женский")
print(human2.info())
