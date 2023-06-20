class Laptop:
    storage="1TB"
    refreshRate="240Hz"
    Graphics="3060"
    def gaming(self):
        print("Gaming")
    def editing(self):
        print("video")
##name=Laptop()
##print(name.storage)
##print(name.refreshRate)
##print(name.gaming)

##class mobile:
##    name="Asus_Rog"
##    storage="128GB"
##    battery="6000MaH"
##    def 

class Monkey:
    breed="Orangutan"
    colour="Orange"
    food="Herbivores"
    def value(self):
        for i in range(len(breed)):
            print(breed[i])
    def valueOne(self):
        for i in range(len(colour)):
            print(colour[i])
##animal=Monkey()
##print(animal.value)

class Human:
    breed="Homosapien"
    colour="Brown"
    food="Omnivores"
    def name(self):
        print(len(breed))
##only=Human()
##print(only.name)
##print(only.colour)

class Building:
    def enter(self):
        print("self=",self)
        print("Swimming pool")
    def setValues(self,size,floor,purpose):
        self.size=size
        self.floor=floor
        self.room=self.floor*3
        self.purpose=purpose
built=Building()
##print(built)
##built.enter()
built.setValues("5000 acres",5,"living")
print(built.floor)
print(built.room)
        
    
