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

def fileReaderTop3(filename):
    """This function takes a text file containing player time as input. It returns the top 3 times for the player, excluding duplicates"""
    try:
        with open(filename, "r") as file:   #Reads in the file, ensures it's formatted properly
            data = file.readline()
            data = data.strip().split(",")
            data = sorted(set([sanitize(line) for line in data]))[0:3]   #Converts to proper time formats, removes duplicates
        return data

    except IOError as err:
        print ("File error: " + str(err))

james = fileReaderTop3("james.txt")
julie = fileReaderTop3("julie.txt")
mikey = fileReaderTop3("mikey.txt")
sarah = fileReaderTop3("sarah.txt")

print(james)
print(julie)
print(mikey)
print(sarah)
     

    