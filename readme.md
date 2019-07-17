# 1 ) Installing Reference

- Install scrapy

  https://docs.scrapy.org/en/latest/intro/install.html#installing-scrapy

  > ```
  > pip install Scrapy
  > ```

- install lxml

  https://lxml.de/installation.html

  > ```
  > sudo apt-get install python3-lxml
  > (For MacOS-X, a macport of lxml is available. Try something like
  > sudo port install py27-lxml)
  > ```

- install w3lib

  https://pypi.org/project/w3lib/

  > pip install w3lib

- Install teisted

  https://twistedmatrix.com/trac/

  > ```
  > $virtualenvtry-twisted
  > $ . try-twisted/bin/activate
  > $ pip install twisted[tls]
  > $ twist --help
  > ```

- Install Cryptography

  https://cryptography.io/en/latest/

  > ```
  > pip install cryptography
  > ```
  >
  > 

- Install pyOpenSSL

  https://pypi.org/project/pyOpenSSL/

  > pip install pyOpenSSL

# 2) Scrapy Tutorial

## a ) Create a project

Before you start scraping, you will have to set up a new Scrapy project. Enter a directory where you’d like to store your code and run:

> ```
> scrapy startproject tutorial
> ```

This will create a `tutorial` directory with the following contents:

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```



## b) How to run our spider

To put our spider to work, go to the project’s top level directory and run:

This can run the book.py
> scrapy crawl book -o output.json

Run the douban.py
> scrapy crawl book