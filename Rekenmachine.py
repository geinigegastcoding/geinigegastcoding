
print("Selecteer een van de onderstaande mogelijkheden om uit te voeren")
print("1. OPTELLEN")
print("2. AFTREKKEN")
print("3. KEER")
print("4. DELEN")
print("5. ")
print("6. ")
operation = input()

if operation == "1":
    num1 = input("Voer het 1ste nummer in: ")
    num2 = input("Voer het 2de nummer in: ")
    print("Het andtwoord is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Voer het  1ste nummer in: ")
    num2 = input("Voer het  2de nummer in: ")
    print("Het andtwoord is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Voer het 1ste nummer in: ")
    num2 = input("Voer het 2de nummer in: ")
    print("Het andtwoord is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Voer het 1ste nummer in: ")
    num2 = input("Voer het 2de nummer in: ")
    if int(num2) == 0 or int(num1) == 0:
        print("Je kan niet delen door nul probeer opnieuw")
    else:
        print("Het andtwoord is " + str(int(num1) / int(num2)))
elif operation == "69":
    print("je bent niet grappig")
elif operation == "kanker" or "homo" or "flikker" or "tyfus" or "tering":
    print("niet schelden")
else:
    print("Invalid Entry")

input("Druk op Enter om af te sluiten...")