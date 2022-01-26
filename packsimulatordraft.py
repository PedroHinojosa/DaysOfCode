import random

class Card(object):
    """A trading card"""
   
    def __init__(self, is_autograph = True):
        FIRSTN = ["Lamelo","Michael","Troy","Shaq"]
        LASTN = ["Ball", "Jordan", "Aikman", "O'Neal"]
        
        self.playername = random.choice(FIRSTN) + " " + random.choice(LASTN)
        self.autograph = is_autograph
        
    def __str__ (self):
        if self.autograph == True:
            rep = self.playername + " , Signed Autograph"
            return rep
        else:
            rep = self.playername + ", Unsigned"
            return rep
    
    def __eq__(self,other):
        return self.playername == other.playername and self.autograph
    
    def __hash__(self):
        return hash(('name', self.playername, 'auto', self.autograph))

class Pack(object):
    """A pack object containing a set number of card objects"""

    def __init__(self):
        self.cards = []

    
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "   "
        else:
            rep = "<empty>"
        return rep
    
    def generate(self, numCards = 5):
        for cds in range(numCards):
            self.auto = random.randint(0,1)
            self.gencard = Card(self.auto)
            self.cards.append(self.gencard)
            
    
class Collection(object):
    """Tracks cards collected"""

    def __init__(self):
        self.library = []
    
    def __str__(self):
        if self.library:
            rep = ""
            for card in self.library:
                rep += str(card) + "   "
        else:
            rep = "<empty>"
        return rep
    
    def add(self, pack):
        self.library.extend(pack.cards)
        self.seen_cards=set()
        self.new_list = []
        
        for obj in self.library:
            if hash(obj) not in self.seen_cards:
                self.new_list.append(obj)
                self.seen_cards.add(hash(obj))
        
        self.library = self.new_list
            
    def show_collection(self):
       for i, item in enumerate(self.library,0):
        print(i, '. ' + str(item), sep='',end='\n')



#main
my_collection = Collection()

pack1=Pack()
pack1.generate()

my_collection.add(pack1)

my_collection.show_collection()






