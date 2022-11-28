#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '/home/hubert/Documents/pelican-themes/Flex'

AUTHOR = 'Hubert J. Banville'
SITENAME = 'Hubert J. Banville'
SITETITLE = AUTHOR
SITESUBTITLE = '<b>AI Research Scientist</b> @ Meta AI'
SITEDESCRIPTION = 'Academic website and blog'
SITELOGO = '/images/me.jpg'
BROWSER_COLOR = '#333333'
THEME_COLOR = '#FF8000'
PYGMENTS_STYLE = 'default'
SITEURL = ''
GITHUB_URL = 'https://github.com/hubertjb'

STATIC_PATHS = ['images']

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', 'https://github.com/hubertjb'),
          ('linkedin', 'https://linkedin.ca/in/hubertbanville'),
          ('book', 'https://scholar.google.com/citations?user=Qoh3xVgAAAAJ&hl=en'),
          ('twitter', 'https://twitter.com/hubertjbanville'))

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 150

COPYRIGHT_YEAR = 2022

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
