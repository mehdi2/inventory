from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Displays a hello message!!!"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Hello, this is your custom command!'))

