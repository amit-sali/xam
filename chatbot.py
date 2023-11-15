import os
import time

def wishme():
    now = time.localtime()
    if now.tm_hour < 12:
        print("Good Morning Sir")
    elif 12 <= now.tm_hour <= 16:
        print("Good Afternoon sir")
    else:
        print("Good Evening sir")

def datetime():
    now = time.ctime()
    print("The date and time is ")
    print(now)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("\t\t\t<============================= W E L C O M E =============================>")
    print("\t\t\t<============================= I'M A VIRTUAL ASSISTANT =============================>")
    
    password = ""
    ch = ""

    while True:
        print("=======================")
        print("| ENTER YOUR PASSWORD |")
        print("=======================")

        password = input("Enter your password: ")

        if password == "admin":
            print("\n<==================================================================================================>\n")
            wishme()

            while True:
                print("\n<==================================================================================================>\n")
                print("How can I help you, sir....")
                print("Your query ===> ")
                ch = input()

                if ch.lower() in ["hi", "hey", "hello"]:
                    print("Hello sir.....")
                elif ch.lower() in ["bye", "stop", "exit"]:
                    print("Good Bye sir, have a nice day!!!!")
                    exit(0)
                elif ch.lower() in ["who are you", "tell me about yourself", "about"]:
                    print("I'm a virtual assistant created by Aditi !!!")
                elif ch.lower() in ["how are you", "whatsup", "how is your day"]:
                    print("I'm good sir, tell me how can I help you..")
                elif ch.lower() in ["time", "date"]:
                    datetime()
                elif ch.lower() == "open notepad":
                    print("Opening Notepad.....")
                    os.system("notepad")
                elif ch.lower() == "open google":
                    print("Opening Google.....")
                    os.system("start https://www.google.com")
                elif ch.lower() == "open youtube":
                    print("Opening YouTube.....")
                    os.system("start https://www.youtube.com")
                elif ch.lower() == "open instagram":
                    print("Opening Instagram.....")
                    os.system("start https://www.instagram.com")
                else:
                    print("Sorry, could not understand your query. Please try again!!!")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("\t\t\t<============================= W E L C O M E =============================>")
            print("\t\t\t<============================= I'M VIRTUAL ASSISTANT =============================>")
            print("X Incorrect Password X\n")
