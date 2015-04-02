from importd import d
from path import path
from datetime import datetime

from djangothis.app import dotslash, read_yaml, watchfile

posts = None


def get_posts():
    global posts
    if posts is not None:
        return posts
    posts = []

    _posts = path(dotslash("_posts"))
    if not _posts.exists():
        return posts

    for post in _posts.walkfiles():
        if post.endswith(".swp"):
            continue
        watchfile(post)
        content = post.open().read()
        _, header, body = content.split("---", 2)
        body = body.replace("{% include JB/setup %}", "")
        header = read_yaml(header)
        y, m, d, slug = post.basename().split("-", 3)
        slug = slug[:-3]
        url = header.get("url", "/%s/%s/%s/" % (y, m, slug))
        posts.append({
            "date": datetime(int(y), int(m), int(d)),
            "url": url,
            "title": header["title"],
            "header": header,
            "body": body,
            "section": header.get("section", ""),
        })
    posts.sort(lambda x, y: cmp(x["date"], y["date"]), reverse=True)
    return posts


def context_processor(request):
    return {
        "settings": d.settings,
        "posts": get_posts(),
    }


def find_post_by_path(pth):
    prev, curr, nex = None, None, None
    for post in get_posts():
        if curr:
            nex = post
            break
        if post["url"] == pth:
            curr = post
        else:
            prev = post
    if not curr:
        raise d.Http404
    return prev, curr, nex


@d(".*")
def post_page(request):
    prev, curr, nex = find_post_by_path(request.path)
    return "post.html", {
        "previosu": prev,
        "post": curr,
        "next": nex
    }
