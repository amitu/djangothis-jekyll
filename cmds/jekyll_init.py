from django.core.management.base import NoArgsCommand
from djangothis.path import path

from _theme.cmds import create_post, create_page # dunno abt _theme name

config_yaml = """
author:
    name: <your name>
    twitter: <twitter_handle>
    github: <github_handle>
    email: <email>

site:
    name: Your New djangothis Site
    production_url: <final url>

TEMPLATE_CONTEXT_PROCESSORS:
    - django.core.context_processors.request
    - django.contrib.auth.context_processors.auth
    - _theme.views.context_processor
"""

index_html = """
<ul class="posts">
    {% for post in posts %}
        <li>
            <span>{{ post.date|date:"d M Y"}}</span> &raquo;
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endfor %}
</ul>
"""

dummy_post_md = """
---
layout: post
title:  "Welcome to Jekyll!"
---

You'll find this post in your `_posts` directory - edit this post To add new
posts:

{% highlight shell %}
$ djangothis jekyll_post "Title of the post"
{% endhighlight %}

djangothis also offers powerful support for code snippets:

{% highlight python %}
def print_hi(name):
  print "Hi", name

print_hi("Amit")

# prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [djanogthis docs][https://github.com/amitu/djangothis] for more
info on how to get the most out of djangothis. File all bugs/feature requests
at [djanogthis's GitHub repo][https://github.com/amitu/djangothis/issues].

"""

dummy_post_title = "Welcome To djangothis!"

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
            create_page(url="index.html", title="Blog", content=index_html)

        # archive, tags, categories etc will be handled by views.py in future.
        # create _posts with one dummy post
        if path("_posts").exists():
            print "_posts exists, skipping."
        else:
            create_post(dummy_post_title, dummy_post_md)

        print 'All Done.'
        print 'Run "djangothis jekyll_post" or "djangothis jekyll_page".'

