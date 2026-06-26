from menu import dish_name, drink_name, dessert_name
import random
order = {}


class bill:

    def __init__(self):
        self.order_id = None
        self.customer_id = None
        self.option_ordered = []
        self.total_bill = 0


    def create_order_id(self, customer_id):

        while True:
            order_id = random.randint(500, 900)

            if order_id not in order:
                self.order_id = order_id
                break

        self.customer_id = customer_id
        self.option_ordered = []
        self.total_bill = 0

        print(f"Order ID {self.order_id} created successfully.")


    def add_option_in_bill(self, item_id):

        if item_id in dish_name:
            item_name, price = dish_name[item_id]

        elif item_id in drink_name:
            item_name, price = drink_name[item_id]

        elif item_id in dessert_name:
            item_name, price = dessert_name[item_id]

        else:
            print("Item number not found.")
            return

        self.option_ordered.append((item_id, item_name, price))
        self.total_bill += price

        print(f"{item_name} added successfully.")


    def delete_option_in_bill(self, item_id):

        for item in self.option_ordered:

            if item[0] == item_id:

                self.option_ordered.remove(item)
                self.total_bill -= item[2]

                print("Item removed successfully.")
                return

        print("Item not found.")


    def print_bill(self):

        print("\n RECEIPT")

        print(f"Order ID : {self.order_id}")

        if self.customer_id is None:
            print("Customer : Guest")
        else:
            print(f"Customer ID : {self.customer_id}")

        print("-" * 60)

        for item_id, item_name, price in self.option_ordered:

            print(f"{item_id:<5}{item_name:.<45}€{price:.2f}")

        print("-" * 60)
        print(f"Total Bill : €{self.total_bill:.2f}")

        order[self.order_id] = {
            "customer_id": self.customer_id,
            "items": self.option_ordered,
            "total": self.total_bill
        }
