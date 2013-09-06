from django.core.management.base import CommandError
from django.template.defaultfilters import slugify

from string import Template
from datetime import date

from djangothis.path import path

post_template = Template(
"""---
layout: post
title: "$title"
---
{% include JB/setup %}

$content

"""
)

def create_post(title, content=""):
    today = date.today()
    pth = "_posts/%s-%02d-%02d-%s.md" % (
        today.year, today.month, today.day, slugify(title)
    )
    if not path("_posts").exists():
        path("_posts").makedirs()
    if path(pth).exists():
        raise CommandError("Post already exists")
    content = post_template.substitute(title=title, content=content)
    file(pth, "w").write(content)
    print pth, "created."

page_template = Template(
"""
{% extends "page.html" %}
{% block title %}$title{% endblock %}
{% block page_content %}
{% filter md %}

$content

{% endfilter %}
{% endblock %}
""".strip()
)

def create_page(title, url, content=""):
    if url.startswith("/"):
        url = url[1:]
    if url.endswith("/"):
        url += "index.html"
    if not url.endswith(".html"):
        url += ".html"
    if path(url).exists():
        raise CommandError("%s already exists." % url)
    if path(url).parent:
        path(url).parent.makedirs()
    content = page_template.substitute(title=title, content=content)
    file(url, "w").write(content)
    print url, "created."

