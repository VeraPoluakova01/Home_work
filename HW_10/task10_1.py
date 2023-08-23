"""Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. """


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


class Factory:

    def create_animal(self, kind, name, age, spec):
        if kind.lower() == "fishes":
            return Fishes(kind, name, age, spec)
        elif kind.lower() == "birds":
            return Birds(kind, name, age, spec)
        elif kind.lower() == "mammals":
            return Mammals(kind, name, age, spec)
        else:
            raise ValueError("Данный тип отсутствует.")


factory = Factory()

fishes = factory.create_animal("fishes", "Немо", 5, 15)
birds = factory.create_animal("birds", "Жемчужина", 10, "голубой")
mammals = factory.create_animal("mammals", "Мэни", 7, "бивни")

print(fishes.get_animal_info())
print(birds.get_animal_info())
print(mammals.get_animal_info())
