from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from djangothis.path import path

from _theme.cmds import create_post

class Command(BaseCommand):
    help = 'Create a new post'

    def handle(self, *args, **options):
        if len(args) == 0:
            raise CommandError("Title of post required.")
        title = " ".join(args)
        title = title.strip()
        create_post(title=title, content="")

