class Animals:
    def type(self,animalName,typeName,coating,food):
        self.animalName=animalName
        self.typeName=typeName
        self.coating=coating
        self.food=food
    def display(self):
        print("animal name is",self.animalName,self.typeName,self.coating,self.food)

    def poison (self):
        self.name=input("Enter the name: ")

    def venom (self):
        if name=="Reptiles":
            print("Some Reptiles are poisonous, eg: Snakes")
        elif name=="Mammals":
            print("Some mammals are dangerous, eg: Lion, Tiger")
        else:
            print("All animals are good in thier own nature")

    def examples (self,Reptiles,Mammals,Birds):
        self.Reptiles=Reptiles
        self.Mammals=Mammals
        self.Birds=Birds

    def pets(self):
        for i in len(varietyTwo):
            print(varietyTwo[i])

    def Oviporus(self):
        print("Egg laying animals are called Oviporus")

creatures=Animals()
print(creatures.Oviporus)
creatures.examples("Snakes","Dogs","Crow")
print(creatures.Mammals)
creatures.type("Elephant","Mammal","HairlessSkin","Herbivore")
print(creatures.animalName)
print(creatures.venom)
creatures.display()




        
