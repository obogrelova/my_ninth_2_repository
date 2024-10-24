# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных
# и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} ({self.species})"

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name} ({animal.species})")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name} ({animal.species})")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"В зоопарк добавлено животное: {animal.name} ({animal.species})")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"В зоопарк принят сотрудник: {staff_member.name}")

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f" - {animal.name} ({animal.species})")

    def show_staff(self):
        print(f"Сотрудники зоопарка {self.name}:")
        for member in self.staff:
            print(f" - {member.name}")

zookeeper = ZooKeeper("Анна")
vet = Veterinarian("Доктор Иван")
tiger = Animal(name="Тигр", species="Амурский тигр")
parrot = Animal(name="Попугай", species="Ара")

zoo = Zoo(name = "Зоопарк Мечта")

zoo.add_animal(tiger)
zoo.add_animal(parrot)
zoo.add_staff(zookeeper)
zoo.add_staff(vet)