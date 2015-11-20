#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

ROOT_DIR = 'D:\\Sem\\Dropbox\\semenkov.su'

import os
import sys
sys.path.append(ROOT_DIR)
from pelican_local_conf import *


SITEURL = 'http://semenkov.su'
RELATIVE_URLS = False

OUTPUT_PATH = 'D:\\inetpub\\wwwroot\\semenkov_upload\\'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'semenkov-su'
YANDEX_ANALYTICS = '30667434'
#GOOGLE_ANALYTICS_UNIVERSAL = 'UA-2819309-3'
#GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'