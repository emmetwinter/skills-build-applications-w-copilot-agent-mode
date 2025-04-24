from django.core.management.base import BaseCommand
import json
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        try:
            # Connect to MongoDB
            client = MongoClient("mongodb://localhost:27017/")
            db = client["octofit_db"]

            # Load test data from JSON file
            with open('octofit-tracker/backend/octofit_tracker/test_data.json', 'r') as file:
                data = json.load(file)

            # Populate collections with error handling
            if 'users' in data:
                db.users.insert_many(data['users'])
            else:
                self.stdout.write(self.style.WARNING('No users data found in test_data.json.'))

            if 'teams' in data:
                db.teams.insert_many(data['teams'])
            else:
                self.stdout.write(self.style.WARNING('No teams data found in test_data.json.'))

            if 'activities' in data:
                db.activity.insert_many(data['activities'])
            else:
                self.stdout.write(self.style.WARNING('No activities data found in test_data.json.'))

            if 'leaderboard' in data:
                db.leaderboard.insert_many(data['leaderboard'])
            else:
                self.stdout.write(self.style.WARNING('No leaderboard data found in test_data.json.'))

            if 'workouts' in data:
                db.workouts.insert_many(data['workouts'])
            else:
                self.stdout.write(self.style.WARNING('No workouts data found in test_data.json.'))

            self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
