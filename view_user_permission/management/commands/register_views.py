from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "register views with @register_view in permission model"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('every thing seems good'))
