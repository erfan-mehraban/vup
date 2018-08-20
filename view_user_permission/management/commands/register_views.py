from django.core.management.base import BaseCommand, CommandError
from view_user_permission.models import Permission
from view_user_permission.register import registered_views
class Command(BaseCommand):
    help = "register views with @register_view in permission model"
    # force django to check all system so view registeration in
    #   view_user_permission.register.registered_views will be done
    requires_system_checks = True

    def handle(self, *args, **options):
        for view_name in registered_views:
            self.stdout.write(view_name+" registered")
            for action in Permission.action_map:
                Permission.objects.get_or_create(view=view_name, action=action[0])
        self.stdout.write(self.style.SUCCESS('done'))
