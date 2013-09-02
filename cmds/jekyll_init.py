from django.core.management.base import NoArgsCommand
from djangothis.path import path

from _theme import create_post, create_page # dunno abt _theme name

config_yaml = """
"""

index_html = """
"""

dummy_post_md = """
"""

dummy_post_title = ""

class Command(NoArgsCommand):
    help = 'Initialize basic files and folders'

    def handle_noargs(self, **options):
        # create empty config.yaml
        if path("config.yaml").exists():
            print "config.yaml exists, skipping."
        else:
            file("config.yaml", "w").write(config_yaml)

        # create index.html
        if path("index.html").exists():
            print "index.html exists, skipping."
        else:
            create_page(index_html)

        # archive, tags, categories etc will be handled by views.py in future.
        # create _posts with one dummy post
        if path("_posts").exists():
            print "_posts exists, skipping."
        else:
            create_post(dummy_post_title, dummy_post_md)

        print 'All Done.'
        print 'Run "djangothis jekyll_post" or "djangothis jekyll_page".'
