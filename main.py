class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} випускає звук")

    def fly(self):
        print(f"{self.name} летить")

class Cage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.birds = []

    def add_bird(self, bird):
        if len(self.birds) < self.capacity:
            self.birds.append(bird)
            print(f"{bird.name} доданий у клітку")

    def simulate(self):
        for bird in self.birds:
            bird.make_sound()
            bird.fly()

parrot = Bird("Жовтик", "Папуга")
sparrow = Bird("Хмарка", "Горобець")

cage = Cage(2)

cage.add_bird(parrot)
cage.add_bird(sparrow)

cage.simulate()
