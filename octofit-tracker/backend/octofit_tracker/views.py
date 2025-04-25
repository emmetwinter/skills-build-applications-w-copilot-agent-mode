from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserListView(APIView):
    def get(self, request):
        users = []  # Fetch users from MongoDB
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class TeamListView(APIView):
    def get(self, request):
        teams = []  # Fetch teams from MongoDB
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class ActivityListView(APIView):
    def get(self, request):
        activities = []  # Fetch activities from MongoDB
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class LeaderboardListView(APIView):
    def get(self, request):
        leaderboard = []  # Fetch leaderboard from MongoDB
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)

class WorkoutListView(APIView):
    def get(self, request):
        workouts = []  # Fetch workouts from MongoDB
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/'
    })