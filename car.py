import datetime


def car(user_input):
    _running = False

    while(user_input != "quit"):

        if(user_input == "help"):
            print(f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} >",
                  "Commands:\n",
                  "<START> - starts the engine\n",
                  "<STOP> - stops the engine\n",
                  "<HELP> - shows engine commands\n",
                  "<QUIT> - exits\n")

        elif(user_input == "start"):
            if(not _running):
                _running = True
                print(
                    f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} > START ENGINE")
            else:
                print(
                    f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} > INVALID COMMAND. ENGINE already started.")

        elif(user_input == "stop"):
            if(_running):
                _running = False
                print(
                    f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} > STOP ENGINE")
            else:
                print(
                    f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} > INVALID COMMAND. ENGINE already stopped.")

        else:
            print(f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} >",
                  "Command not found. Type 'HELP' for engine commands or 'QUIT' to exit")

        user_input = input().lower()

    print(f"{datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')} > Exit")


car(input().lower())
