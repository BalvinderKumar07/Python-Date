import getpass

def get_wifi_password():
    password = getpass.getpass("Enter Wi-Fi password: ")
    return password

def main():
    while True:
        print("1. Show Wi-Fi password")
        print("2. Hide Wi-Fi password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password = get_wifi_password()
            print("Wi-Fi password:", password)
        elif choice == '2':
            print("Wi-Fi password: ********")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

    

