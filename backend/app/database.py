import csv
import os
from typing import List, Dict

DB_FILE = "loan_record.csv"  # Name of our data storage file

def save_record(record: Dict) -> None:
    """Saves one loan application to our CSV file"""
    file_exists = os.path.isfile(DB_FILE)  # Check if file already exists
    
    with open(DB_FILE, 'a', newline='') as f:  # Open file in append mode
        writer = csv.DictWriter(f, fieldnames=record.keys())
        if not file_exists:  # If new file, write header row first
            writer.writeheader()
        writer.writerow(record)  # Add the new record

def get_records() -> List[Dict]:
    """Reads all loan records from our CSV file"""
    if not os.path.isfile(DB_FILE):  # If file doesn't exist
        return []  # Return empty list
        
    with open(DB_FILE, 'r') as f:  # Open file for reading
        reader = csv.DictReader(f)  # Create CSV reader
        return list(reader)  # Return all records as dictionaries