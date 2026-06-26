import csv
from customer_data import Customer, registered_customers


class FileManager:

    def save_customers(self):

        with open("customers.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Customer ID",
                "Name",
                "Phone Number",
                "Email",
                "Loyalty Points"
            ])

            for customer in registered_customers.values():

                writer.writerow([
                    customer.customer_id,
                    customer.name,
                    customer.phone_number,
                    customer.email_id,
                    customer.loyalty_points
                ])

        print("Customers saved successfully.")

    def load_customers(self):

        registered_customers.clear()

        try:

            with open("customers.csv", "r") as file:

                reader = csv.reader(file)

                next(reader, None)

                for row in reader:

                    customer = Customer(
                        int(row[0]),
                        row[1],
                        row[2],
                        row[3]
                    )

                    customer.loyalty_points = int(row[4])

                    registered_customers[customer.customer_id] = customer

            print("Customers loaded successfully.")

        except FileNotFoundError:

            print("No customer data found.")
