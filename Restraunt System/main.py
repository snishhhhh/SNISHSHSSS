from menu import Menu
from customer_data import customer 
from customer_data import registed_customer
from reservation import Table_reservation
from generate_bill import bill
import sys

Restaurent_menu= Menu()
Customer= customer(None, "", "", "")
Reservation= Table_reservation()
Bill= bill()

while True:
    print("==============RESTAURENT SYSTEM===============\n")
    print("1. View Menu\n"
          "2. Register a Customers\n"
          "3. Make Reservation\n"
          "4. Generate Bill")
    choice= input("Please select the option number you want to execute: ")
    if choice=="1":
        Restaurent_menu.full_menu()
    elif choice=="2":
        name= input("Customer Name: ")
        phone= input("Phone Number: ")
        email= input("Email ID: ")
        Customer.registration(name, phone, email)
    elif choice=="3":
        Reservation.make_reservation()
    elif choice=="4":
        answer= input(" Is the customer registred(Y/N): ")
        if answer=="Y":
            customer_id= int(input("Enter Customer ID: "))
            if customer_id not in registed_customer:
                print ("Customer ID not found")
                continue
            Bill.creat_order_id(customer_id)
            Restaurent_menu.full_menu()
            
            while True:
                option=int(input("Enter the item number to add"))
                if option==0:
                    break
                Bill.add_options_in_bill(option)
            Bill.print_bill()
            Customer.reward_points(customer_id, Bill.total_bill)
            Customer.add_order(Bill.order_id)
                
        elif answer=="N":
            Bill.creat_order_id(None)
            Restaurent_menu.full_menu()
            while True:
                option=int(input("Enter the item number to add"))
                if option==0:
                    break
                Bill.add_options_in_bill(option)
            Bill.print_bill()
            
    else:
        sys.exit()
            
        
    
            
        
    