import csv
import os
import datetime

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

# function to make reservation
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
    print([table['Number'] for table in available_tables])
    if table_number not in [table['Number'] for table in available_tables]:
        print("Invalid table number.")
        return
    
    new_row = [table_number, name, party_size, contact, date, start_time, end_time]
    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
            print(writer)

        print(f"Table {table_number} reserved successfully for {name} on {date} from {start_time} to {end_time}.")
    except Exception as e:
        print(f"Error saving reservations: {e}")
    
# make_reservation(Tables, reservations_file)


# def cancel_reservation(reservations_file):
#     table_number = input("Enter table number to cancel: ")
#     if table_number in [reservations_file]:
#         del reservations [table_number]
#         print("Reservation cancelled")


def view_reservation(reservations_file):
    with open(reservations_file,mode= 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
# view_reservation(reservations_file)

def modify_reservation(reservations_file):
    table_number = int(input("Enter the table number to modify"))
    date = input("Enter current date")
    name = input("Enter current reservation name:")

    try:
        with open(reservations_file,mode= 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)

        modified_reservations = []
        reservation_found = False

        for res in reservations:
            if res[header.index('Table Number')] == table_number and res[header.index('name')] == name and res[header.index('party_size')] == party_size:
                reservation_found = True
                print('Reservation found')

                new_name = input("Enter your name: ")
                new_contact = input("Enter your contact number: ")
                new_party_size = int(input("Enter your party size: "))
                new_date = input("Enter reservation date (YYYY-MM-DD): ")
                new_start_time = input("Enter reservation start time (HH:MM): ")
                new_end_time = input("Enter reservation end time (HH:MM): ")

                modified_reservations.append(res)

        if reservation_found:
            with open(reservations_file, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(modified_reservations)
            print("Reservation modified")
        else:
            print("No reservation found")
    except Exception as e:
        print(f"Error modifying reservation: {e}")

def daily_summary(reservations_file, date):
    with open(reservations_file,mode= 'r') as file:
        reader = csv.reader(file)
        summary = [row for row in reader if datetime.strptime(row['date'], '%Y-%m-%d') == datetime.strptime('2024-07-05', '%Y-%m-%d')]
        print(summary)

        #datetime.strptime(row['date'], '%Y-%m-%d') converts the 'date' to a datetime object
        

            # if new_name:
            #     res[header.index('name')] = new_name
            # if new_contact:
            #     res[header.index('contact')] = new_contact
            # if new_party_size:
            #     res[header.index('party_size')] = new_party_size
            # if new_date:
            #     res[header.index('date')] = new_date
            # if new_start_time:
            #     res[header.index('start_time')] = new_start_time
            # if new_end_time:
            #     res[header.index('end_time')] = new_end_time

    # modify_reservation(reservations_file)
    
    # with open (reservations_file, mode= 'r') as file:
    #     reader = csv.reader(file)
    #     header = next(reader)
    #     reservations = list(reader)
    # 
def main():
    print("\n1. Make reservation\n2. Cancel reservation\n3. View reservation\n4. Modify reservation\n5. View daily summary")

    choice = int(input("Choose an option:"))
    if choice == 1:
        make_reservation(Tables, reservations_file)
    elif choice == 2:
        cancel_reservation(reservations_file)
    elif choice == 3:
        view_reservation(reservations_file)
    elif choice == 4:
        modify_reservation(reservations_file)
    elif choice == 5:
        daily_summary(reservations_file)
    else:
        print("Invalid input")

main()
            
                                                                                             