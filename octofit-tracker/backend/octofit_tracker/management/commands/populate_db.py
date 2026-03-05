from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Direct MongoDB cleanup
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboards.delete_many({})
        db.workouts.delete_many({})

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel', is_superhero=True)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel', is_superhero=True)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_superhero=True)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc', is_superhero=True)

        # Create activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='fly', duration=60, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
        Workout.objects.create(name='Flight Training', description='Aerial skills', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
