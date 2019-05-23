import datetime as d
# please create 6 files named
# ankit_diet.txt
# ankit_exercise.txt
# sumit_diet.txt
# sumit_exercise.txt
# vaibhav_diet.txt
# vaibhav_exercise.txt


def get_action():
    action= int(input("Please Choose Action\n"))
    data=""
    if (action == 1):
        data= input("Please type here what you want to insert\n")
        return "write", data
    elif(action == 2):
        return "read", data
    else:
        print("Please enter 1 or 2")
        get_action()

def get_activity():
    activity = int(input("Please Choose Activity\n"))
    if (activity == 1):
        return "diet"
    elif (activity == 2):
        return "exercise"
    else:
        print("Please enter 1 or 2")
        get_activity()

def getusername():
    no = int(input("Please Enter user number\n"))
    if(no == 1):
        return "Ankit"
    elif(no == 2):
        return "Sumit"
    elif(no == 3):
        return "Vaibhav"
    else:
        print("Please enter 1-3")
        getusername()

def readfile(name, activity):
    filename = name + "_" + activity + ".txt"
    with open(filename) as f:
        a = f.read()
        return a

def appenttofile(name, activity, text):
    filename = name + "_" + activity + ".txt"
    date= str(d.datetime.now())
    f = open(filename,"a")
    f.write("\n"+date+" : "+text)
    f.close()

print("=======================:  Hiii Welcome to health management portal  :==================\n")
def run():
    print("Please press\n 1 for Ankit \n 2 for Sumit \n 3 for Vaibhav")
    name= getusername()

    print("Please choose action \n 1 for Diet and\n 2 for Exercise")
    activity= get_activity()

    print("Please choose activity \n press 1 to insert data and\n press 2 if you want to see your data")
    action, text=get_action()

    if action == "write":
        appenttofile(name,activity,text)
        print("Congrats you have successfully inseted data")
    else:
        out= readfile(name,activity)
        print("Here are your content\n"+out)

    next = input("Do you want to continue.\n Press 'Y' to continue\n Press'N' to exit\n")
    if next == "Y" or next =="y":
        run()
    else:
        exit()

run()



