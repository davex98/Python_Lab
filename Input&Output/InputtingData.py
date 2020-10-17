def displayInput(name, surname, birthdate):
    print("Your name is {} {}, and you have been born on {}.".format(name, surname, birthdate))


if __name__ == "__main__":
    data = input("Enter your name, surname and birthdate: ").split()
    displayInput(*data)
