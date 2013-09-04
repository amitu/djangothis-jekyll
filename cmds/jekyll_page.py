from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from djangothis.path import path

from _theme.cmds import create_page

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '--title',
            help='Title Of The Page'
        ),
        make_option(
            '--url',
            help='URL Of The Page'
        ),
    )
    help = 'Create a new page'

    def handle(self, *args, **options):
        if not (options["title"] and options["url"]):
            raise CommandError("Both --title and --url are required")
        create_page(title=options["title"], url=options["url"], content="")

