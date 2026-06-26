# Main Courses
dish_name = {
    101: ("Truffle Pasta", 12.99),
    102: ("Chicken Burger", 7.80),
    103: ("Chicken Soup", 5.50),
    104: ("Garlic Butter Bread", 6.00),
    105: ("Prosciutto Pizza", 10.50),
    106: ("Garlic Mushroom Rice", 7.99),
    107: ("Crispy Chicken Wings", 6.70),
    108: ("Coconut Chicken Curry", 12.50),
    109: ("BBQ Pork Burger", 8.50),
    110: ("Smoked Wings", 6.00)
}

# Drinks
drink_name = {
    201: ("Mango Lassi", 4.50),
    202: ("Oreo Milkshake", 5.50),
    203: ("House White Wine", 6.00),
    204: ("Pineapple Mocktail", 4.50),
    205: ("Peach Bellini", 4.50),
    206: ("Espresso Martini", 5.50)
}

# Desserts
dessert_name = {
    301: ("Classic Tiramisu", 4.50),
    302: ("Vanilla Bean Creme Brulee", 5.60),
    303: ("Chocolate Lava Cake", 4.50),
    304: ("Salted Caramel Cheesecake", 6.80),
    305: ("Pistachio Gelato", 3.50)
}


class Menu:

    # Display one category
    def print_prices(self, category, items):

        print(f"\n{category}")
        print("-" * 60)

        for item_id, (item_name, price) in items.items():
            print(f"{item_id:<5}{item_name:.<45}€{price:.2f}")


    # Display the complete menu
    def full_menu(self):

        self.print_prices("MAIN COURSES", dish_name)
        self.print_prices("DRINKS", drink_name)
        self.print_prices("DESSERTS", dessert_name)


    # Search for an item
    def search_option(self, option_id):

        if option_id in dish_name:
            item_name, price = dish_name[option_id]

        elif option_id in drink_name:
            item_name, price = drink_name[option_id]

        elif option_id in dessert_name:
            item_name, price = dessert_name[option_id]

        else:
            print("Item not found.")
            return

        print("\nItem Found")
        print(f"Name : {item_name}")
        print(f"Price: €{price:.2f}")


    # Modify an existing item
    def modify_option(self, option_id, new_name, new_price):

        if option_id in dish_name:
            dish_name[option_id] = (new_name, new_price)

        elif option_id in drink_name:
            drink_name[option_id] = (new_name, new_price)

        elif option_id in dessert_name:
            dessert_name[option_id] = (new_name, new_price)

        else:
            print("Item not found.")
            return

        print("Item modified successfully.")


    # Delete an item
    def delete_option(self, option_id):

        if option_id in dish_name:
            del dish_name[option_id]

        elif option_id in drink_name:
            del drink_name[option_id]

        elif option_id in dessert_name:
            del dessert_name[option_id]

        else:
            print("Item not found.")
            return

        print("Item deleted successfully.")


    # Add a new item
    def add_option(self, option_id, item_name, price):

        if (option_id in dish_name or
                option_id in drink_name or
                option_id in dessert_name):

            print("Item number already exists.")
            return

        if 100 <= option_id < 200:

            dish_name[option_id] = (item_name, price)
            print("Main course added successfully.")

        elif 200 <= option_id < 300:

            drink_name[option_id] = (item_name, price)
            print("Drink added successfully.")

        elif 300 <= option_id < 400:

            dessert_name[option_id] = (item_name, price)
            print("Dessert added successfully.")

        else:

            print("Invalid item number.")






        
