from tkinter import *

class Application(Frame):
    """A GUI Application with 3 buttons"""

    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        #create third button 
        Label(self, text = "Choose your favorite type of movie").grid(row = 0, column = 0, sticky = W)
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    
    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Total clicks " + str(self.bttn_clicks) 


#Create root window
root = Tk()
root.title("Click Counter")
root.geometry("110x110")

#Instantiate
app = Application(root)

#Kick off the window's event loop
root.mainloop()
