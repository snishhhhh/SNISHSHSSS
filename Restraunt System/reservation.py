from datetime import datetime
import random


reservations = {}


class TableReservation:

    def __init__(self):

        self.reservation_id = None
        self.name = ""
        self.phone_number = ""
        self.number_of_people = 0
        self.date = ""
        self.time = ""
        self.table = 0
        self.date_and_time = None

    def make_reservation(self):

        self.name = input("Enter customer name: ")
        self.phone_number = input("Enter phone number: ")
        self.number_of_people = int(input("Enter number of guests: "))
        self.date = input("Enter reservation date (YYYY-MM-DD): ")
        self.time = input("Enter reservation time (HH:MM): ")
        self.table = int(input("Enter table number: "))

        self.date_and_time = datetime.strptime(
            f"{self.date} {self.time}",
            "%Y-%m-%d %H:%M"
        )

        while True:

            reservation_id = random.randint(1000, 9999)

            if reservation_id not in reservations:
                self.reservation_id = reservation_id
                break

        reservations[self.reservation_id] = self

        print("\nReservation created successfully.")
        print(f"Reservation ID: {self.reservation_id}")

    # View reservation
    def view_reservation(self):

        reservation_id = int(input("Enter reservation ID: "))

        if reservation_id not in reservations:
            print("Reservation not found.")
            return

        reservation = reservations[reservation_id]

        print("\n===== RESERVATION DETAILS =====")
        print(f"Reservation ID : {reservation.reservation_id}")
        print(f"Customer Name  : {reservation.name}")
        print(f"Phone Number   : {reservation.phone_number}")
        print(f"Guests         : {reservation.number_of_people}")
        print(f"Date & Time    : {reservation.date_and_time}")
        print(f"Table Number   : {reservation.table}")

    # Modify reservation
    def modify_reservation(self):

        reservation_id = int(input("Enter reservation ID: "))

        if reservation_id not in reservations:
            print("Reservation not found.")
            return

        reservation = reservations[reservation_id]

        print("\nEnter new details")

        reservation.name = input("Customer Name: ")
        reservation.phone_number = input("Phone Number: ")
        reservation.number_of_people = int(input("Guests: "))
        reservation.date = input("Date (YYYY-MM-DD): ")
        reservation.time = input("Time (HH:MM): ")
        reservation.table = int(input("Table Number: "))

        reservation.date_and_time = datetime.strptime(
            f"{reservation.date} {reservation.time}",
            "%Y-%m-%d %H:%M"
        )

        print("Reservation updated successfully.")


    def delete_reservation(self):

        reservation_id = int(input("Enter reservation ID: "))

        if reservation_id in reservations:

            del reservations[reservation_id]

            print("Reservation deleted successfully.")

        else:

            print("Reservation not found.")

   
        
        
    
        
        
            
    
