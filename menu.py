def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[0] Exit the program.")


    menu()
    option = int(input("Enter your option: "))

    while option != 0:
        if option == 1:
            #do option 1 stuff
            print("option 1 has been called.")
        elif option == 2:
            #do option 2 stuff
            print("option 2 has been called.")
        else:
            print("Invalid Option.")

        print()
        menu()
        option = int(input("Enter your option: "))

print("Thanks. Goodbye")                    