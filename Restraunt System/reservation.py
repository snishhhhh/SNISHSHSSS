from datetime import datetime
import random
reservations=[]
class Table_reservation:
    def __init__(self):
        self.name= ""
        self.phone_number= ""
        self.number_of_people= ""
        self.date= ""
        self.time= ""
        self.reservation_id= None
        self.table= 0
        self.date_and_time= None
        
    def make_reservation(self):
        self.name= input("Enter the name of the reserver: " )
        self.phone_number= input("Enter the reserver phone number: ")
        self.number_of_people= int(input("Enter the number of guest being reserved: "))
        self.date= input ("Enter the Date for reservation (yyyy-mm-dd): ")
        self.time= input("Enter the Time for reservation (hh:mm): ")
        self.table= int(input("Please enter table number you want to reserv: "))
        self.date_and_time= datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        while True:
            reservation_id=random.randint(1000,9999)
            if not any(r.reservation_id== reservation_id for r in reservations):
                self.reservation_id= reservation_id
                break
        reservations.append(self)
        print(f"You have booked a reservation sucssefully, here is your reservation number: {self.reservation_id}")
    def modify_reservation(self):
        reservation_id= int(input("Provide reservation number of reservation you want to modify: "))
        for reservation in reservations:
            if reservation.reservation_id== reservation_id:
                print ("\nPlease provide new details: " )
                reservation.name= input("Enter the name of the reserver: " )
                reservation.phone_number= input("Enter the reserver phone number: ")
                reservation.number_of_people= int(input("Enter the number of guest being reserved: "))
                reservation.date= input ("Enter the Date for reservation (yyyy-mm-dd): ")
                reservation.time= input("Enter the Time for reservation (hh:mm): ")
                reservation.table= int(input("Please enter table number you want to reserv: "))
                reservation.date_and_time= datetime.strptime(f"{reservation.date} {reservation.time}", "%Y-%m-%d %H:%M")
                print("Reservation updated sucssefully")
                return
        
        print("Reservation number not found")
    def delete_reservation(self):
        reservation_id= int(input("Please input the reservation number you want to delete: "))
        for reservation in reservations:
            if reservation.reservation_id== reservation_id:
                reservations.remove(reservation)
                print("Reservation deleted sucssefully")
                return
        print("Reservation number not found")
    def view_reservation(self):
        reservation_id= int(input("Please input the reservation number: "))
        for reservation in reservations:
            if reservation.reservation_id== reservation_id:
                print(f"reserver name: {reservation.name}\n",
                      f"Reserver phone number:{reservation.phone_number}\n",
                      f"Guest number: {reservation.number_of_people}\n"
                      f"Reserved date and time: {reservation.date_and_time}\n",
                      f"Reserved table number: {reservation.table}\n" )
                return
        print("Reservation number not found")

   
        
        
    
        
        
            
    