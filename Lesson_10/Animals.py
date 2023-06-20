"""
- Создайте три (или более) отдельных классов животных.
Например, рыбы, птицы и т.п.
- У каждого класса должны быть как общие свойства.
Например, имя, так и специфичные для класса.
- Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""
import random


class Animal():
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def move(self):
        pass

    def say(self):
        pass

    def showInfo(self):
        pass


class Bird(Animal):
    wings = 2

    def __init__(self, name: str, weight: int, bird_type: str):
        super().__init__(name, weight)
        self.bird_type = bird_type

    def move(self):
        return 'is flying'

    def say(self):
        return f'{self.bird_type} says dee-dee-dee'

    def showInfo(self):
        return f'Name={self.name}, Weight={self.weight}, Wings={self.wings}, Type={self.bird_type}'


class Fish(Animal):
    gills = 2
    fins = 2

    def __init__(self, name: str, weight: int, fish_type: str):
        super().__init__(name, weight)
        self.fish_type = fish_type

    def move(self):
        return 'is swimming'

    def say(self):
        return f'{self.fish_type} says something, but you dont understand it'

    def showInfo(self):
        return f'Name={self.name}, Weight={self.weight}, Gills={self.gills}, Type={self.fish_type}'


class Cat(Animal):
    legs = 4

    def __init__(self, name: str, weight: int, cat_type: str):
        super().__init__(name, weight)
        self.cat_type = cat_type

    def move(self):
        return 'is running'

    def say(self):
        return f'{self.cat_type} says meow-meow'

    def showInfo(self):
        return f'Name={self.name}, Weight={self.weight}, Legs={self.legs}, Type={self.cat_type}'


class Factory():
    nameList = []

    def create_nameList(self):
        counter = 1
        while (counter < 50):
            self.nameList.append(f'Animal-{counter}')
            counter += 1

    def __init__(self, animal_type: str):
        self.animal_type = animal_type
        self.create_nameList()

    def create_animal(self):
        nameNumber = random.randint(0, len(self.nameList) - 1)
        name = self.nameList[nameNumber]
        if (self.animal_type.lower() == 'bird'):
            return Bird(name, random.randint(1, 10), self.animal_type)
        elif (self.animal_type.lower() == 'cat'):
            return Cat(name, random.randint(1, 10), self.animal_type)
        elif (self.animal_type.lower() == 'fish'):
            return Fish(name, random.randint(1, 10), self.animal_type)


def mainMethod():
    bird1 = Factory('bird').create_animal()
    cat1 = Factory('cat').create_animal()
    fish1 = Factory('fish').create_animal()
    print(bird1.showInfo())
    print(cat1.showInfo())
    print(fish1.showInfo())


mainMethod()
