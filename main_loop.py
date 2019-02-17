# Define Functions


# Function that handles all litre conversions
def litreconv():
    print("you have selected Litres")
    conversion = int(input("input Litres to convert: "))
    print(str(conversion) + " Litres")
    converted = 0.21997 * conversion
    print(str(round(converted, 4)) + " UK Gallons")
    converted = conversion / 3.785
    print(str(round(converted, 4)) + "US Gallons")


# Function that handles all UK Gallon conversions
def ukgallonconv():
    print("You have selected UK Gallons")
    conversion = int(input("Input UK Gallons to convert: "))
    print(str(conversion) + " UK Gallons")
    converted = conversion / 0.21997
    print(str(round(converted, 4)) + " Litres")
    converted = conversion * 1.201
    print(str(round(converted, 4)) + "US Gallons")


# Function that handles all US Gallon conversions
def usgallonconv():
    print("You have selected US Gallons")
    conversion = int(input("input US Gallons to convert: "))
    print(str(conversion) + " US Gallons")
    converted = conversion * 3.785
    print(str(round(converted, 4)) + " Litres")
    converted = conversion / 1.201
    print(str(round(converted, 4)) + " UK Gallons")


# Function that handles Pearsons Square calculation. Note: Tidy variable/input names
def pearsonsconv():
    pearsontarget = float(input("Please enter your target percentage: "))
    print("You entered " + str(pearsontarget))
    pearsoninput1 = float(input("Please enter your top left number: "))
    print("You entered " + str(pearsoninput1))
    pearsoninput2 = float(input("Please enter your bottom left number: "))
    print("You entered " + str(pearsoninput2))
    if pearsoninput2 > pearsontarget:
        pearsonsum2 = pearsoninput2 - pearsontarget
    else:
        pearsonsum2 = pearsontarget = pearsoninput2

    print("Top right: " + str(pearsonsum2))
    if pearsoninput1 > pearsontarget:
        pearsonsum1 = pearsoninput1 - pearsontarget
    else:
        pearsonsum1 = pearsontarget - pearsoninput1

    print("Bottom right = " + str(pearsonsum1))
    pearsonsumtotal = pearsonsum1 + pearsonsum2
    print("Total of the two: " + str(pearsonsumtotal))
    pearsonsum2 = (pearsonsum2 / pearsonsumtotal) * 100
    print("Top right percentage: " + str(pearsonsum2))
    pearsonsum1 = (pearsonsum1 / pearsonsumtotal) * 100
    print("Bottom right percentage: " + str(pearsonsum1))


# Function that outputs needed amount of Potassium Metabisulphate from desired amount of sulphur dioxide
def sulphurdioxideconv():
    print("You have selected Potassium Metabisulphate > Sulphur Dioxide")
    so2=float(input("Please input the required amount of Sulphur Dioxide:"))
    print("You entered" + str(so2))
    so2sum = (so2 / 57) * 100
    print("You require " + str(so2sum) + "mg of Potassium Metabisulphate")


# Main Loop
firstrun = 0
run = 1
# On first open shows instructions. Will be redundant after UI added.
while firstrun == 0:
    print("Welcome to WineConverter.")
    print("Enter 'List' to see the available conversions, and then either enter the number or the name of the measurement you have.")
    print("To Quit enter 'Quit' or 'Exit'\nTo see these instructions again enter 'Help'")
    firstrun = 1
# Main loop, user inputs command to call function
while run == 1:
    command = input("Please enter your command: ")
    command.lower()
    if command == "list":
        print("1. Litres\n2. UK Gallons\n3. US Gallons\n 4. Pearsons Square\n5. Sulphur Dioxide")
    elif command == "litres" or command == "1":
        litreconv()
    elif command == "uk gallons" or command == "2":
         ukgallonconv()
    elif command == "us gallons" or command == "3":
        usgallonconv()
    elif command == "pearsons" or command == "4":
        pearsonsconv()
    elif command =="Sulphur" or command == "5":
        sulphurdioxideconv()
    elif command == "exit" or command == "quit":
        run = 0
    else:
        print("Command not recognised, please enter List to see a full list of commands")
