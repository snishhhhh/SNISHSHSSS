from menu import Menu
from customer_data import Customer, registered_customers
from reservation import TableReservation
from generate_bill import bill
from File_Managing_system import FileManager
import sys

restaurant_menu = Menu()
reservation = TableReservation()
Bill = bill()
file_manager = FileManager()


file_manager.load_customers()

while True:

    print("\n RESTAURANT MANAGEMENT SYSTEM ")
    print("1. View Menu")
    print("2. Register Customer")
    print("3. View Customer Details")
    print("4. Make Reservation")
    print("5. View Reservation")
    print("6. Generate Bill")
    print("7. View Customer Order History")
    print("8. Search Menu Item")
    print("9. Modify Menu Item")
    print("10. Delete Menu Item")
    print("11. Add Menu Item")
    print("12. Save Customer Data")
    print("13. Load Customer Data")
    print("14. Exit")

    choice = input("\nSelect an option: ")


    if choice == "1":

        restaurant_menu.full_menu()


    elif choice == "2":

        name = input("Customer Name: ")
        phone = input("Phone Number: ")
        email = input("Email Address: ")

        customer = Customer(None, "", "", "")
        customer.registration(name, phone, email)


    elif choice == "3":

        customer_id = int(input("Enter Customer ID: "))

        if customer_id in registered_customers:

            registered_customers[customer_id].display_customer()

        else:

            print("Customer not found.")


    elif choice == "4":

        reservation.make_reservation()


    elif choice == "5":

        reservation.view_reservation()


    elif choice == "6":

        answer = input("Is the customer registered? (Y/N): ").upper()

        if answer == "Y":

            customer_id = int(input("Enter Customer ID: "))

            if customer_id not in registered_customers:

                print("Customer not found.")
                continue

            customer = registered_customers[customer_id]

            Bill.create_order_id(customer_id)

            restaurant_menu.full_menu()

            while True:

                option = int(input("Enter Item Number (0 to Finish): "))

                if option == 0:
                    break

                Bill.add_option_in_bill(option)

            Bill.print_bill()

            customer.reward_points(Bill.total_bill)

            customer.add_order(Bill.order_id)

        elif answer == "N":

            Bill.create_order_id(None)

            restaurant_menu.full_menu()

            while True:

                option = int(input("Enter Item Number (0 to Finish): "))

                if option == 0:
                    break

                Bill.add_option_in_bill(option)

            Bill.print_bill()

        else:

            print("Invalid choice.")
            

    elif choice == "7":

        customer_id = int(input("Enter Customer ID: "))

        if customer_id in registered_customers:

            registered_customers[customer_id].view_order_history()

        else:

            print("Customer not found.")


    elif choice == "8":

        option_id = int(input("Enter Item Number: "))

        restaurant_menu.search_option(option_id)


    elif choice == "9":

        option_id = int(input("Enter Item Number: "))
        new_name = input("Enter New Item Name: ")
        new_price = float(input("Enter New Price: "))

        restaurant_menu.modify_option(option_id, new_name, new_price)


    elif choice == "10":

        option_id = int(input("Enter Item Number: "))

        restaurant_menu.delete_option(option_id)

    elif choice == "11":

        option_id = int(input("Enter New Item Number: "))
        item_name = input("Enter Item Name: ")
        price = float(input("Enter Item Price: "))

        restaurant_menu.add_option(option_id, item_name, price)


    elif choice == "12":

        file_manager.save_customers()


    elif choice == "13":

        file_manager.load_customers()


    elif choice == "14":

        file_manager.save_customers()

        print("\nCustomer data saved successfully.")
        print("Thank you for using the Restaurant Management System.")

        sys.exit()

    else:

        print("Invalid option. Please try again.")
        
    
            
        
    
