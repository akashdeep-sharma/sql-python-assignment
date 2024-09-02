import csv
import os
import statistics
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load and clean data from a CSV file into the Product table'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['file']

        if not os.path.isfile(csv_file_path):
            self.stdout.write(self.style.ERROR(f'The file {csv_file_path} does not exist'))
            return

        # Load the data into a list to process missing values
        data = []
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert price, quantity_sold, and rating to numeric values
                row['price'] = self.to_float(row['price'])
                row['quantity_sold'] = self.to_int(row['quantity_sold'])
                row['rating'] = self.to_float(row['rating'])
                data.append(row)

        # Handle missing values
        self.clean_data(data)

        # Save cleaned data to the database
        for row in data:
            Product.objects.create(
                product_name=row['product_name'],
                category=row['category'],
                price=row['price'],
                quantity_sold=row['quantity_sold'],
                rating=row['rating'],
                review_count=row['review_count'],
            )

        self.stdout.write(self.style.SUCCESS('Data loaded and cleaned successfully into the Product table'))

    def to_float(self, value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    def to_int(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def clean_data(self, data):
        # Calculate medians for price and quantity_sold
        prices = [row['price'] for row in data if row['price'] is not None]
        quantities = [row['quantity_sold'] for row in data if row['quantity_sold'] is not None]
        price_median = statistics.median(prices) if prices else 0
        quantity_median = statistics.median(quantities) if quantities else 0

        # Calculate average ratings per category
        category_ratings = {}
        for row in data:
            if row['category'] not in category_ratings:
                category_ratings[row['category']] = []
            if row['rating'] is not None:
                category_ratings[row['category']].append(row['rating'])

        category_avg_rating = {cat: statistics.mean(ratings) for cat, ratings in category_ratings.items()}

        # Replace missing values
        for row in data:
            if row['price'] is None:
                row['price'] = price_median
            if row['quantity_sold'] is None:
                row['quantity_sold'] = quantity_median
            if row['rating'] is None:
                row['rating'] = category_avg_rating.get(row['category'], 0)
