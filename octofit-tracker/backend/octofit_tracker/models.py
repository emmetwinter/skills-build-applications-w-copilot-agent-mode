from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Example collections
users_collection = db["users"]
teams_collection = db["teams"]
activity_collection = db["activity"]
leaderboard_collection = db["leaderboard"]
workouts_collection = db["workouts"]

# Define Python classes to represent data models
class User:
    def __init__(self, email, name, age):
        self.email = email
        self.name = name
        self.age = age

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

class Activity:
    def __init__(self, user_email, activity_type, duration, date):
        self.user_email = user_email
        self.activity_type = activity_type
        self.duration = duration
        self.date = date

class Leaderboard:
    def __init__(self, user_email, points):
        self.user_email = user_email
        self.points = points

class Workout:
    def __init__(self, name, description, duration):
        self.name = name
        self.description = description
        self.duration = duration