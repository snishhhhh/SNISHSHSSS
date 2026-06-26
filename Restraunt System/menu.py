#names with prices and option number of the options as it eases ordering process
dish_name={ 
101:("Truffle Pasta", 12.99),
102:("Chicken Burger", 7.80),
103:("Chicken Soup", 5.50),
104:("Garlic Butter Bread (1 bugatte per serv)", 6.00),
105:("Proscuitto Pizza", 10.50),
106:("Garlic Mushroom Rice", 7.99),
107:("Crispy Chicken Wings (4 wings)", 6.70),
108:("Coconuct Chicken Curry", 12.50),
109:("BBQ Pork Burger", 8.50),
110:("Smoked Wings(4 wings)", 6.00)}

drink_name={201:("mango lassi", 4.50),
202:("Oreo Milkshakes", 5.50),
203:("House White Wine", 6.00),
204:("Pineapple Mocktail", 4.50),
205:("Peach Bellini", 4.50),
206:("Espresso Martini", 5.50)}

dessert_name={301:("Classic Tiramisu", 4.50),
302:("Vanilla Bean Crème Brûlée", 5.60),
303:("Chocolate Lava Cake", 4.50),
304:("Salted Caramel Cheesecake", 6.80),
305:("Pistachio Gelato", 3.50)}
# Making a clean layout to display prices 
# according to each option in the menue
class Menu:
    def print_prices(self, catogery, options):
        print(f"\n{catogery}")
        print("-"*40)
        for iteam_id, (item, price)in options.items():
            print (f"{iteam_id:<5}" f"{item:.<45}" f"€{price:.2f}")   
# combining whole menue as one             
    def full_menu(self):
        self.print_prices("MAIN COURSE", dish_name)
        self.print_prices("BEVERAGES", drink_name)
        self.print_prices("DESSERTS", dessert_name)
# Here we are adding a method to modify existing options on menu
    def modify_options(self, option_id, modified_option_name, new_price, ):
        if option_id in dish_name:
            dish_name[option_id]= (modified_option_name, new_price)
            print("Modified sucsessfully")
        elif option_id in drink_name:
            drink_name[option_id]= (modified_option_name, new_price)
            print("Modified sucsessfully")
        elif option_id in dessert_name: 
            dessert_name[option_id]= (modified_option_name, new_price)
            print("Modified sucsessfully") 
        else:
            print("Invalid, please recheck your option number")   
#This method is for deleting existing options
    def delete_option(self, option_id):
        if option_id in dish_name:
            del dish_name[option_id]
            print("Deleted sucsessfully")
        elif option_id in drink_name:
            del drink_name[option_id]
            print("Deleted sucsessfully")
        elif option_id in dessert_name: 
            del dessert_name[option_id]
            print("Deleted sucsessfully")
        else:
            print("Invalid, please recheck your option number")  
# search method to serch for option with ease
    def search_option(self, option_id):
        if option_id in dish_name:
            option_name, price= dish_name[option_id]
            print(f"found item:")
            print(f"Name:{option_name}")
            print(f"Price:€{price:.2f}")
            
        elif option_id in drink_name:
            option_name, price= drink_name[option_id]
            print(f"found item:")
            print(f"Name:{option_name}")
            print(f"Price:€{price:.2f}")
            
        elif option_id in dessert_name: 
            option_name, price= dessert_name[option_id] 
            print(f"found item:")
            print(f"Name:{option_name}")
            print(f"Price:€{price:.2f}")
            
        else:
            print("Invalid, please recheck your option number") 
# Add method to add new options
    def add_options(self, option_id, new_option_name, price):
        if option_id in dish_name or drink_name or dessert_name:
            print("Couldn't add Number already exists")
            return
        elif 100<= option_id<200:
            dish_name[option_id]= (new_option_name, price)
            print ("Main Course added sucsessfully")
        elif 200<=option_id<300: 
            drink_name[option_id]= (new_option_name, price)
            print ("Beverage added sucsessfully")
        elif 300<=option_id<400:
            dish_name[option_id]= (new_option_name, price)
            print ("Dessert added sucsessfully")
        else:
            print("Invalid") 
                    
               
            
                
           


 









        