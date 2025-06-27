import csv
from collections import defaultdict
from datetime import datetime

def load_transactions(file_path):
    transactions = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Amount'] = float(row['Amount'])
            row['Date'] = datetime.strptime(row['Date'], "%Y-%m-%d")
            transactions.append(row)
    
    return transactions

def summarize_by_category(transactions):
    summary = defaultdict(float)
    for tx in transactions:
        category = tx['Category']
        amount = tx['Amount']
        summary[category] += amount
    return dict(summary)

def summarize_by_period(transactions, period='month'):
    summary = defaultdict(float)

    for tx in transactions:
        date = tx['Date']
        amount = tx['Amount']
        if period == 'month':
            key = date.strftime("%Y-%m")
        elif period == 'year':
            key = date.strftime("%Y")
        else:
            key = date.strftime("%Y-%m-%d")
        summary[key] += amount
    
    return dict(summary)
