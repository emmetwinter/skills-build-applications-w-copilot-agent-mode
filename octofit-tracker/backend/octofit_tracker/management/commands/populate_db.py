from django.core.management.base import BaseCommand
import json
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Load test data from JSON file
        with open('octofit-tracker/backend/octofit_tracker/test_data.json', 'r') as file:
            data = json.load(file)

        # Populate collections
        db.users.insert_many(data['users'])
        db.teams.insert_many(data['teams'])
        db.activity.insert_many(data['activities'])
        db.leaderboard.insert_many(data['leaderboard'])
        db.workouts.insert_many(data['workouts'])

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
