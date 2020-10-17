
if __name__ == '__main__':
    newPassword = input("Set up your password: ")
    attempts = 0
    while attempts < 3:
        verifiedPassword = input("Verify your password: ")
        if newPassword != verifiedPassword:
            print("Access denied! Try again")
            attempts += 1
        else:
            print('Access granted')
            break
