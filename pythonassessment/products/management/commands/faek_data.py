import csv
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the categories you want to use
categories = [
    'Electronics', 'Home Appliances', 'Books', 'Clothing', 'Toys', 
    'Sports Equipment', 'Beauty Products', 'Automotive', 'Furniture', 'Groceries'
]

# Generate fake data
def generate_fake_data(num_records):
    with open('fake_products.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow([
            'product_name', 
            'category', 
            'price', 
            'quantity_sold', 
            'rating', 
            'review_count'
        ])

        for _ in range(num_records):
            product_name = fake.word().capitalize() + " " + fake.word().capitalize()
            category = random.choice(categories)
            price = round(random.uniform(10.0, 1000.0), 2)
            quantity_sold = random.randint(1, 500)
            rating = round(random.uniform(1.0, 5.0), 1)
            review_count = random.randint(0, 1000)
            
            # Write the row
            writer.writerow([
                product_name, 
                category, 
                price, 
                quantity_sold, 
                rating, 
                review_count
            ])

    print(f"{num_records} fake records written to 'fake_products.csv'")

# Generate 100 fake records
generate_fake_data(100)
