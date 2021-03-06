import pickle

from athletelist import Athlete

def get_coach_data(filename):
    """This function takes a text file containing player time as input. Returns a dictionary with Name, DOB, and fastest times"""
    try:
        with open(filename, "r") as file:   #Reads in the file, ensures it's formatted properly
            data = file.readline()
        data = data.strip().split(",")
        
        return (Athlete(data.pop(0), data.pop(0), data))

    except IOError as err:
        print ("File error: " + str(err))

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open("athletes.pickle", "wb") as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print("File error (put_and_store):" + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle","rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print("File error (get_from_store):" + str(ioerr))
    return(all_athletes)




    
