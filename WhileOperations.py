#   The program will tell if the car status


command = ""
started = False
stopped = False
while True:
    command = raw_input("> ").lower()
    if command == "start":
        if started:
            print("Car is started already")
        else:
            started = True
            print("Car Started ...")
    elif command == "stop":
        if stopped:
            print("Car is stopped already!!")
        else:
            stopped = True
            print("Car Stopped!!..")
    elif command == "help":
        print('''
        start  to start the car
        stop   to stop the car
        help   for more info''')
    elif command == "quit":
        break
    else:
        print("Invalid command")
