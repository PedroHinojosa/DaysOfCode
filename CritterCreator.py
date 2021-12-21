#Simple Critter Creator
#Demonstrates a basic class, objects, constructors, private/public methods, etc.

class Critter(object):
    """A Virtual Pet"""

    total = 0

    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)
    
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name= name
        Critter.total +=1
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name =="":
            print("A critter's name can't be an empty string")
        else:
            self.__name = new_name
            print("Name Change Successful")

    def talk(self):
        print("Hi. I'm ", self.name, "\n")
    
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep


#main
print ("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)

print("\nCreating Critters.")
crit1 = Critter("Critter 1")
crit2 = Critter("Critter 2")
crit3 = Critter("Critter 3")

Critter.status()

print("\nAccessing the class attribute through an object:", end=" ")
print(crit1.total)

crit=Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end=" ")
print(crit.name)

crit.name="Randolph"
print("\nMy critter's name is:", end=" ")
print(crit.name)

input("\n\nPress the enter key to exit")


