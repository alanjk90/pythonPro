weight = int(input("Enter your weight: "))
wtype = input("Enter the type of Weight:")
if wtype == "L":
    result = weight * 10
    print(result)

elif wtype == "W":
    result = weight / 10
    print(result)

else:
    print("Enter the correct option")
