# getinput = input("Enter your option")
# print(getinput)
# count = 1
command = ""
while command != "quit":
    command = input(">")
    print("done")
    if command == "start":
        print("Car started")

    elif command == "stop":
        print("car stoped")
    elif command == "quit":
        break
