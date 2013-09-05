from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from djangothis.path import path

from _theme.cmds import create_page

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '--url',
            help='URL Of The Page'
        ),
    )
    help = 'Create a new page'

    def handle(self, *args, **options):
        if len(args) == 0:
            raise CommandError("Title of page required.")
        title = " ".join(args)
        title = title.strip()
        if not options["url"]:
            raise CommandError("--url is required.")
        create_page(title=title, url=options["url"], content="")

