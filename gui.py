from tkinter import *

class Application(Frame):
    """A GUI Application with 3 buttons"""

    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        """Create three buttons that do nothing"""
        #create first button
        self.bttn1 = Button(self, text = "I do nothing")
        self.bttn1.grid()

        #create second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Me Too!")

        #create third button 
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"


#Create root window
root = Tk()
root.title("Lazy Buttons")
root.geometry("110x110")

#Instantiate
app = Application(root)

#Kick off the window's event loop
root.mainloop()
