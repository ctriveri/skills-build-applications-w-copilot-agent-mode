from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=spiderman, type='cycle', duration=45)
        app_models.Activity.objects.create(user=batman, type='swim', duration=60)
        app_models.Activity.objects.create(user=superman, type='run', duration=50)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio session for all')
        app_models.Workout.objects.create(name='Strength Training', description='Strength session for all')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=ironman, points=100)
        app_models.Leaderboard.objects.create(user=spiderman, points=90)
        app_models.Leaderboard.objects.create(user=batman, points=95)
        app_models.Leaderboard.objects.create(user=superman, points=110)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
