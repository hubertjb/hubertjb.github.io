#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '/home/hubert/Documents/pelican-themes/Flex'

AUTHOR = 'Hubert J. Banville'
SITENAME = 'Hubert J. Banville'
SITESUBTITLE = 'PhD student @ Inria, Parietal Team <br> Biosignal Researcher @ InteraXon Inc.'
SITEDESCRIPTION = 'Academic website and blog'
SITELOGO = ''
FAVICON = '/images/favicon.png'
BROWSER_COLOR = '#333333'
THEME_COLOR = '#FF8000'
PYGMENTS_STYLE = 'default'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Parietal Team', 'https://team.inria.fr/parietal/'),
#         ('Muse Research', 'https://choosemuse.com/muse-research/'),
#         ('NeuroTechX', 'https://neurotechx.com/'))

# Social widget
SOCIAL = (('github', 'https://github.com/hubertjb'),
          ('linkedin', 'https://linkedin.ca/in/hubertbanville'),
          ('scholar', 'https://scholar.google.com/citations?user=Qoh3xVgAAAAJ&hl=en'))

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 150

COPYRIGHT_YEAR = 2019

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
