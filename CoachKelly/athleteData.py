class Athlete(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name =  a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

def sanitize(time_string):
    """This function takes a line of time input and makes sure it is in 0.0 format """
    if "-" in time_string:   #Splits the input if it includes a "-" instead of "."
        splitter = "-"
    elif ':' in time_string: #Splits the input if it includes a ":" instead of "."
        splitter  = ":"
    else:
        return(time_string)  #Otherwise returns the input if it is already in "0.0" format
    
    (mins, secs) = time_string.split(splitter) #Takes the split elements and combines them in the return statement
    return (mins + "." + secs)   

def get_coach_data(filename):
    """This function takes a text file containing player time as input. Returns a dictionary with Name, DOB, and fastest times"""
    try:
        with open(filename, "r") as file:   #Reads in the file, ensures it's formatted properly
            data = file.readline()
        data = data.strip().split(",")
        
        return (Athlete(data.pop(0), data.pop(0), data))

    except IOError as err:
        print ("File error: " + str(err))

def displayTimes(c):
    "Displays the player's name and fastest times"
    print (c.name + "'s fastest times are: " + str(c.top3()))

james = get_coach_data("james2.txt")
julie = get_coach_data("julie2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")

displayTimes(james)

james.append(".5")

displayTimes(james)
    