# management/commands/import_books.py
import csv
from django.core.management.base import BaseCommand
from aiEngineerTask.models import StockModel
import pandas as pd


# python manage.py input_csv path/to/your/csv/file.csv

class Command(BaseCommand):
    help = 'Import books from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('stock_market_data.csv', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['stock_market_data.csv']
        
        try:
            df = pd.read_csv('stock_market_data.csv')
        except pd.errors.ParserError as e:
        # Handle the parsing error
            print("Parsing Error:", e)
        # Specify the number of rows to skip
            skip_rows = 892  # skip up to the problematic row
        
        # Read the CSV file again, skipping the problematic rows using the csv module
            with open('stock_market_data.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for _ in range(skip_rows):
                    next(reader)  # Skip the problematic rows
            
            # Read the remaining rows into DataFrame
                df = pd.DataFrame(reader)


    # Convert 'date' column to datetime type
                df['date'] = pd.to_datetime(df['date'])

    # Remove commas and convert other columns to float type
                columns_to_convert = ['high', 'low', 'open', 'close', 'volume']
                df[columns_to_convert] = df[columns_to_convert].replace(',', '', regex=True).astype(float)

    # Convert 'trade_code' column to string type
                df['trade_code'] = df['trade_code'].astype(str)
                for row in df:
                    # Handle missing or invalid dates:
            # try:
            #     dateobj = datetime.datetime.strptime(row['date'], '%Y-%m-%d').date()
            # except ValueError:
            #     print(f"Invalid date format: {row['date']}. Skipping this row.")
            #     continue
            # dateObject = datetime.datetime.strptime(row['date'],'%Y-%m-%d').date()

                    StockModel.objects.create(
                    date=row['date'],
                    trade_code=row['trade_code'],
                    high=row['high'],
                    low=row['low'],
                    open=row['open'],  # Corrected variable name
                    close=row['close'],
                    volume=row['volume'].replace(',', '') if row['volume'] else 0
                    )

        self.stdout.write(self.style.SUCCESS('Books imported successfully'))
