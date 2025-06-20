class Dog:
    def __init__(self,name,breed,age,color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def Sound(self):
        print(self.name,"is barking")

dog1 = Dog("Victory", "German Shephard", 5, "White")
print(dog1.name)
dog1.Sound()

dog2 = Dog("Braxton", "Siberian Husky", 7, "Brown")
print(dog2.breed)

dog3 = Dog("Abigael", "Chihuahua", 10, "Black")
print(dog3.color)












