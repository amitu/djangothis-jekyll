A jekyll like theme for
[djangothis](https://github.com/amitu/djangothis).

Sample site: [amitu.com](http://amitu.com)

#### How to setup your blog

```shell
$ mkdir blog
$ cd blog
$ pip install djangothis
$ git clone git@github.com:amitu/djangothis-jekyll.git _theme

$ # creates config.yaml, index.html, _posts, and sample post
$ djangothis jekyll_init
All Done.
Run "djangothis jekyll_post" or "djangothis jekyll_page".

$ djangothis 
Validating models...

0 errors found
Django version 1.4.1, using settings None
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

To create a new page run:

```shell
$ djanogthis jekyll_page --url="/hello-world/" Hello World
hello-world/index.html created.
```

To create a new post:

```shell
$ djangothis jekyll_post This is a new post
_post/2013-09-02-this-is-a-new-post.md created.
```

To dump the site:

```shell
$ wget -m http://localhost:8000 # while server is running
```

Using gunicorn speeds up mirroring of the site, if you want it then do
the following:

```shell
$ pip install gunicorn
$ djangothis gunicorn # instead of just "djangothis" to run server
```

And then mirror the site using wget.

```shell
$ wget -m http://localhost:8000
```

Enjoy.

#### Attribution

This theme is based on excellent work Yuya Saito, and all other credit
goes to
[jekyllbootstrap](https://github.com/jekyllbootstrap/theme-the-program).

