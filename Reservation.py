import csv
import os

Tables = [
    {'Number': 1, 'seats': 2},
    {'Number': 2, 'seats': 4},
    {'Number': 3, 'seats': 6},
    {'Number': 4, 'seats': 8},
    {'Number': 5, 'seats': 10}
]

reservations_file = 'reservations.csv'
def View_Tables(Tables):
    for Table in Tables:
        print(Table)

View_Tables(Tables)

def make_reservation(Tables, reservations_file):
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    party_size = int(input("Enter number of people: "))
    date = input("Enter reservation date (YYYY-MM-DD): ")
    start_time = input("Enter reservation start time (HH:MM): ")
    end_time = input("Enter reservation end time (HH:MM): ")

    available_tables = [Table for Table in Tables if Table['seats'] >= party_size]

    if  not available_tables:
        print("No available tables for your party size.")
        return
    print("Available tables:")
    for Table in available_tables:
        print(f"Table {Table['Number']} => seats: {Table['seats']}")

    #table to reserve from available list
    table_number = int(input("Enter table number to reserve:"))
    if table_number not in [Table['Number'] for table in available_tables]:
        print("Invalid table number.")
        return
    
    new_row = [table_number, name, party_size, contact, date, start_time, end_time]
    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)

        print(f"Table {table_number} reserved successfully for {name} on {date} from {start_time} to {end_time}.")
    except Exception as e:
        print(f"Error saving reservations: {e}")
    
make_reservation(Tables, reservations_file)

def cancel_reservation(reservations):
    table_number = input("Enter table number to cancel: ")
    if table_number in [reservations_file]:
        del reservations [table_number]
        print("Reservation cancelled")


def view_resevation(reservation):
    