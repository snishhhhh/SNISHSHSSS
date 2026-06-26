import random
from generate_bill import order


registered_customers = {}


class Customer:

    def __init__(self, customer_id, name, phone_number, email_id):

        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.email_id = email_id

        self.order_history = []
        self.loyalty_points = 0


    def registration(self, name, phone_number, email_id):

        while True:

            customer_id = random.randint(1000, 9999)

            if customer_id not in registered_customers:
                break

        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.email_id = email_id


        registered_customers[customer_id] = self

        print(f"\nCustomer registered successfully.")
        print(f"Customer ID : {customer_id}")

    def delete_customer(self, customer_id):

        if customer_id in registered_customers:

            del registered_customers[customer_id]
            print("Customer deleted successfully.")

        else:

            print("Customer ID not found.")


    def reward_points(self, bill_amount):

        reward_points = int(bill_amount // 10) * 5

        self.loyalty_points += reward_points

        print(f"\nReward Points Earned : {reward_points}")
        print(f"Total Loyalty Points : {self.loyalty_points}")


    def add_order(self, order_id):

        self.order_history.append(order_id)


    def view_order_history(self):

        if len(self.order_history) == 0:

            print("No previous orders.")
            return

        print("\n ORDER HISTORY")

        for order_id in self.order_history:

            print(f"\nOrder ID : {order_id}")

            if order_id in order:

                print(order[order_id])


    def display_customer(self):

        print("\n CUSTOMER DETAILS")
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.name}")
        print(f"Phone       : {self.phone_number}")
        print(f"Email       : {self.email_id}")
        print(f"Loyalty     : {self.loyalty_points}")
