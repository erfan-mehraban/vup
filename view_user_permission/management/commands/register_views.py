from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "register views with @register_view in permission model"
    # force django to check all system so view registeration in
    #   view_user_permission.register.registered_views will be done
    requires_system_checks = True

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('every thing seems good'))
