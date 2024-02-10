# import os
# import csv
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import connection
# from .models import StockModel
# import datetime
from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import StockModel
import pandas as pd
import csv
import datetime
from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def load_data_from_csv2():
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




def home(request):
    load_data_from_csv2()
    data = StockModel.objects.all()[:100]
    # chart
    data2 = StockModel.objects.values('date', 'close', 'volume' ).order_by('date')[:10]
    # Extract dates and close prices from queryset
    dates = [entry['date'] for entry in data2]
    close_prices = [entry['close'] for entry in data2]
    volume_prices = [entry['volume'] for entry in data2]
    

    
    # Plot the line chart
    plt.subplot(2, 1, 1)
    plt.plot(dates, close_prices)
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.title('Sample Line Chart')
    # Plot the bar chart
    plt.subplot(2, 1, 2)
    plt.bar(dates, volume_prices)
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Sample Bar Chart')
    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    
    # Pass the base64 string to the template
    # context = {'graphic': graphic}
    return render(request, 'home.html', {'d': data, 'graphic': graphic})

def line_chart(request):
    data = StockModel.objects.values('date', 'close').order_by('date')[:10]
    plt.plot(data['date'], data['close'])
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.title('Sample Line Chart')
    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    
    # Pass the base64 string to the template
    context = {'graphic': graphic}
    return render(request, 'line_chart.html', { context})

def chart_with_dropdown(request):
    trade_code = request.GET.get('trade_code')
    data = StockModel.objects.filter(trade_code=trade_code).values('date', 'close').order_by('date')
    return render(request, 'chart_with_dropdown.html', {'data': data})

def other_visualization(request):
    # Your code for other visualization goes here
    return render(request, 'other_visualization.html')

