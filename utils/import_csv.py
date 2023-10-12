import argparse
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys

sys.path.append("src/edt")
from core.config import config
from models.restaurants import Restaurants

# Define command-line arguments
parser = argparse.ArgumentParser(
    description="Insert data from a CSV file into a PostgreSQL database."
)
parser.add_argument("csv_file", help="Path to the CSV file")

# Parse command-line arguments
args = parser.parse_args()

# Create a SQLAlchemy engine and session
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Open the CSV file and read data
with open(args.csv_file, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        restaurant = Restaurants(
            id=row["id"],
            rating=int(row["rating"]),
            name=row["name"],
            site=row["site"],
            email=row["email"],
            phone=row["phone"],
            street=row["street"],
            city=row["city"],
            state=row["state"],
            lat=float(row["lat"]),
            lng=float(row["lng"]),
        )
        session.add(restaurant)

# Commit the changes to the database
session.commit()

# Close the session
session.close()

print("Data inserted successfully.")
