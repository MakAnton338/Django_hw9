from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()
User = get_user_model()


class Command(BaseCommand):

    help = 'My custom command for create random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(1, 11))

    def handle(self, *args, **options): #** Options- хз что такое
        user = []
        for _ in range(options['count']):
            user.append(User(username=fake.name(), email=fake.email(), password=make_password(fake.password())))
        User.objects.bulk_create(user)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {options["count"]} users'))