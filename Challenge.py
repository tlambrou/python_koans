import sys

class Tiger(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "meat"

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print
        str(self.name), "sleeps for 8 hours"
        return

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        print
        self.name, 'eats', food
        if food == self.favoriteFood:
            print
            'YUM!', self.name, "wants more", food
        return

    # This code tests the Tiger class and its eat and sleep methods
    def test():
        def getline():
            # Read a line from standard input and strip surrounding whitespace
            return sys.stdin.readline().strip()

        # Get the number of animals
        animalCount = int(getline())
        # Iterate through the input for each animal
        for count in range(animalCount):
            # Get the animal's name and food to eat
            name = getline()
            food = getline()
            # Create a Tiger object and test its eat and sleep methods
            tiger = Tiger(name)
            tiger.eat(food)
            tiger.sleep()

    if __name__ == "__main__":
        test()