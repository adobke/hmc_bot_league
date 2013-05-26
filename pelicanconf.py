#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Harvey Mudd Combat Robot Club'
SITENAME = u'HMC Robot League'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'
THEME = "./theme"
#THEME = "../pelican-themes/tuxlite_tbs"

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images']

LINKS =  (('Harvey Mudd College', 'http://www.hmc.edu/'),
          )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['extra','wikilinks','sane_lists','nl2br'])

USE_FOLDER_AS_CATEGORY = False
DELETE_OUTPUT_DIRECTORY = True
