names = set()

while True:
    name = input("Enter a name (or press enter to finish): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")

    names.add(name)

print("\nList of names:")
for name in names:
    print(name)


# 2
airport_data = {}

def enter_new_airport():
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airport_data[icao_code] = airport_name
    print("Airport data has been stored.")

def fetch_airport_info():
    icao_code = input("Enter the ICAO code of the airport to fetch information: ")
    if icao_code in airport_data:
        print("Airport Name:", airport_data[icao_code])
    else:
        print("Airport not found.")

while True:
    print("\nMenu:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        enter_new_airport()
    elif choice == "2":
        fetch_airport_info()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
