from string import Template
from djangothis.path import path
from django.core.management.base import CommandError

post_template = Template(
"""
---
layout: post
title: "$title"
---
{% include JB/setup %}

$content

"""
)

def create_post(title, content=""):
    # TODO: get file url from today and title slug
    pth = ""
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
    content = page_template.substitute(title=title, content=content)
    file(url, "w").write(content)
    print url, "created."

