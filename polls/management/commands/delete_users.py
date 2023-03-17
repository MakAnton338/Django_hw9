from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        user_id = options['user_id']

        if User.objects.filter(pk__in=user_id, is_superuser=True).exists():
            raise CommandError('Error, you try delete superusers')

        users_to_delete_query = Q(pk__in=user_id)
        num_deleted, _ = User.objects.filter(users_to_delete_query).delete()

        self.stdout.write(self.style.SUCCESS(f'Deleted {num_deleted} users with primary keys {user_id}!'))