class Mover(object):
    def __init__(self, legal_moves):
        self.direction= None
    
    def ask_move(self, open_moves):
        self.direction = input("Which way do you want to go?")
        if self.direction in open_moves:
            print("Ok!")
        else:
            print("That was not a legal move!")
        


class Room(Mover):
    def __init__(self, passages, text):
        self.room_look = text
        self.halls=passages
    
    def show_Room(self):
        print(self.room_look)
        

#main
list1=["west","east"]
list2=["north", "south"]
story= "This is a room"
room1 = Room(list1, story)
room1.show_Room()
room1.ask_move(list1)


