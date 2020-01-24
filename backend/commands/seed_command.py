from datetime import datetime
from flask_script import Command

from app import db

from app.transaction import Transaction
import random

def seed_transactions():
    transactions = list()
    for i in range(random.randrange(1, 140)):
        transactions.append(
            {
                "pub_date": datetime(2020, random.randrange(1, 12),
                                     random.randrange(1, 30), 10, 10, 10),
                "amount": random.randrange(1, 256)
            }
        )
    print('i', transactions)
        
    db.session.bulk_insert_mappings(Transaction, transactions)


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        # if (input("Are you sure you want to drop all tables and recreate? (y/N)\n").lower()== "y"):
            # print("Dropping tables...")
        db.drop_all()
        db.create_all()
        seed_transactions()
        db.session.commit()
            # print("DB successfully seeded.")