# Define class
class Dog:

    # Initialization class
    def __init__(self, breed, height, weight):

        self.breed = breed
        self.height = height
        self.weight = weight
        self.height_plus_weight = None

    # Define method for class
    def g(self):

        self.height_plus_weight = self.height + self.weight


# Define function outsie of class that inits a dog and returns it
def f():
    
    x = Dog("Retriever", 0.5, 6.)
    
    return x

dog = f()
dog.height_plus_weight
dog.g()
dog.height_plus_weight

#Hello world function
print("Hello world")
