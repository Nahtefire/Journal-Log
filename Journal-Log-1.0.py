from datetime import datetime
import subprocess
import tempfile


#Declaring variables
    #date color
DateColor = True


#Functions
    #readout input
def getinput():
    with open(n) as f:
        contents = f.read()
        return (contents)
    
    #getting date and time
def gettime():
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S]")
    return dt_string 

    #open and read the file after the appending:
def getlog():
    f = open("JournalLog.txt", "r")
    return (f.read())

def writelog():
    #create and open temp file with nano to take user input
    f = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    n = f.name
    f.close()
    proc = subprocess.call(['nano', n])

    #reads content of file
    with open(n) as f:
        contents = f.read()


    #Combine Date/Time and Text
    if DateColor == True:
        DateAndString = "\u001b[38;5;118m"+gettime()+"\u001b[0m"+contents
    else:
        DateAndString = gettime()+contents
    #Writes input to JournLog file
    f = open("JournalLog.txt", "a")
    f.write(DateAndString + "\n")
    f.close()
    print ("succesfully wrote to file!")
    
programOpen = True
while programOpen == True:
    option = input("What would you like to do?:")
    if option == 'w' or option == 'W' or option == 'write' or option == 'Write':
        writelog()
    elif option == 'r' or option == 'R' or option == 'read' or option == 'Read':
        print (getlog())
    elif option == 'q' or option == 'Q' or option == 'quit' or option == 'Quit':
        programOpen = False
    elif option == 'help':
        print ("w/write = write to journal \n r/read = read whole journal command line \n q/quit = quits program \n help = list of commands")
    else:
        print ("invalid option, type \"help\" for a list of commands")



"""
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
"""
