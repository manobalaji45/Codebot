import json

def read_buses_from_file(filename):
    try:
        with open(filename, "r") as f:
            buses = json.load(f)
        return buses
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        exit()
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filename}.")
        exit()

def search_buses(source, destination, buses):
    # For simplicity, we assume the source and destination filter is not implemented in this basic version
    return buses

def display_buses(buses):
    print("Available Buses:")
    for bus in buses:
        print(f"ID: {bus['id']}, Name: {bus['name']}, Departure: {bus['departure']}, Arrival: {bus['arrival']}, Seats Available: {bus['seats_available']}")

def select_bus(buses):
    while True:
        try:
            bus_id = int(input("Enter the Bus ID to book: "))
            selected_bus = next((bus for bus in buses if bus['id'] == bus_id), None)
            if not selected_bus:
                print("Invalid Bus ID. Please try again.")
            else:
                return selected_bus
        except ValueError:
            print("Invalid input. Please enter a valid Bus ID.")

def collect_passenger_details():
    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    gender = input("Enter passenger gender: ")
    return {"name": name, "age": age, "gender": gender}

def book_ticket(selected_bus, passenger_details):
    booking_details = {
        "bus_id": selected_bus['id'],
        "bus_name": selected_bus['name'],
        "departure": selected_bus['departure'],
        "arrival": selected_bus['arrival'],
        "passenger": passenger_details,
        "status": "confirmed"
    }
    return booking_details

def save_booking(booking, filename="D:/python/read_buses/booking_details.json"):
    try:
        with open(filename, "r") as f:
            existing_bookings = json.load(f)
            if not isinstance(existing_bookings, list):
                print(f"Warning: {filename} did not contain a list. Resetting to an empty list.")
                existing_bookings = []
    except (FileNotFoundError, json.JSONDecodeError):
        existing_bookings = []

    print(f"Existing bookings before appending: {existing_bookings}")
    existing_bookings.append(booking)
    
    with open(filename, "w") as f:
        json.dump(existing_bookings, f, indent=2)
    print(f"Booking details saved to {filename}")

def save_output_to_file(booking, filename="D:/python/read_buses/booking_output.txt"):
    with open(filename, "a") as f:
        f.write("Booking Confirmation:\n")
        f.write(json.dumps(booking, indent=2) + "\n")
    print(f"Booking output saved to {filename}")

if __name__ == "__main__":
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")

    # Step 1: Read buses from file
    buses_file_path = "D:/python/read_buses/buses.json"  # Ensure this path is correct relative to where the script is run
    buses = read_buses_from_file(buses_file_path)
    
    # Step 2: Search for buses
    buses = search_buses(source, destination, buses)
    display_buses(buses)
    
    # Step 3: Select a bus
    selected_bus = select_bus(buses)
    
    # Step 4: Enter passenger details
    passenger_details = collect_passenger_details()
    
    # Step 5: Simulate booking
    booking = book_ticket(selected_bus, passenger_details)
    print(f"Booking confirmed: {json.dumps(booking, indent=2)}")
    
    # Step 6: Store booking details
    save_booking(booking)
    
    # Step 7: Save output to a log file
    save_output_to_file(booking)
