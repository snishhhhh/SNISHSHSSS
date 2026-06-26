#Class to build costumer system for our restaurent
import random
from generate_bill import order
registed_customer = []
class customer:
    def __init__(self, customer_id, name, phone_number, email_id):
        self.customer_id= customer_id
        self.name= name
        self.phone_number= phone_number
        self.email_id= email_id
        self.order_history=[]
        self.loyality_points=0
    def registration(self, name, phone_number, email_id):
        while True:
            customer_id=random.randint(1000,9000)
            if customer_id not in registed_customer:
                break
        registed_customer[customer_id]=(name, phone_number, email_id)
        self.customer_id= customer_id
        print(f"Registration customer ID:{customer_id}")   
         
    def delete_custumer(self,customer_id):
        if customer_id in registed_customer:
            del registed_customer[customer_id]
            print("Registered customer deleted")
        else:
            print("Cutomer ID doesn't exist")
    def reward_points(self, customer_id, bill):
        if customer_id in registed_customer:
            reward_points=int(bill//10)*5
            self.loyality_points+=reward_points
            print(f"You currently have{reward_points} points")
            print(f"You have spent{bill}, aadding up total to {self.loyality_points} points")
        else:
            print("Not a registred customer")
    
    def add_order(self, order_id) :   
        self.order_history.append(order_id)
        
"""def view_order_history(self):
if len(self.order_history) == 0:
print("No previous orders.")
return
for order_id in self.order_history:
print(f"\nOrder ID: {order_id}")
print(order[order_id])"""
        
        #how can i trace back registred costumer to multiple order id