#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ----------------  Semenkov.SU -------------
#
import os

execfile('ya_albums_output.py')

import markdown
from markdown.extensions.toc import TocExtension
from mdimgextension import MdImgExtension

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# переменные для настройки на конкретное рабочее место
#osUSERPROFILE = os.environ['USERPROFILE']
osUSERPROFILE = 'D:\\Sem'
osSYSTEMDRIVE = os.environ['HOMEDRIVE']

AUTHOR = u'SemenS'
SITENAME = u'Semenkov.SU'
SITEURL = 'http://localhost:8080'
SITEMAPURL = 'http://semenkov.su'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_DATE_FORMAT = '%d %B %Y, %A'

DEFAULT_LANG = u'ru'


# --- THEME skeletom --------
THEME = "./pelican-themes/skeleton"


# --- THEME bootstrap 3 --------
# Extra files for bootstrap themes
# CUSTOM_CSS = 'extra/css/naidom.css'
# STATIC_PATHS = ['extra']
# EXTRA_PATH_METADATA = {
    # 'extra/web.config': {'path': 'web.config'},
    # 'extra/favicon.ico': {'path': 'favicon.ico'},
    # }

#THEME = "./pelican-themes/bootstrap3"

#BOOTSTRAP_THEME = "slate"
#BOOTSTRAP_THEME = "paper"
#BOOTSTRAP_THEME = "yeti"
#BOOTSTRAP_THEME = "flatly"
#BOOTSTRAP_THEME = "readable-big"
#BOOTSTRAP_THEME = "spacelab-big"
#BOOTSTRAP_THEME = "spacelab"
#BOOTSTRAP_NAVBAR_INVERSE = True

SERIES_TEXT = u'Эта статья %(index)s-я часть из серии  "%(name)s"'
OUTPUT_PATH = osSYSTEMDRIVE+'\\inetpub\\wwwroot\\naidom\\'
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = (False)

DISPLAY_TAGS_INLINE = True
#DISPLAY_TAGS_ON_SIDEBAR = True
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# это мой параметр для картинок в индексе
SHOW_TITLE_IMG = True	

DIRECT_TEMPLATES = [
'index', 'categories', 'authors', 'archives', 
#'cards'
]
PAGINATED_DIRECT_TEMPLATES = ['index']
#TEMPLATE_PAGES = {'cards.html': 'cards.html' }

# Feed generation is usually not desired when developing
#FEED_DOMAIN = 'http://semenkov.su'
FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None


PHOTO_ALBUMS = {u'YA': ya_albums }

MD_EXTENSIONS =  [ 
    TocExtension(title='Содержание'),
	MdImgExtension(photos=PHOTO_ALBUMS),
    'codehilite','extra','admonition'
]


DEFAULT_PAGINATION = 12


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# Папка с общими (едиными) для всех плагинами

PLUGIN_PATHS = [osUSERPROFILE+'\\Dropbox\\pelican\\plugins\\']
PLUGINS = [	'md_metayaml', 	'series', 'sitemap', 'tag_cloud','iobjects' ]

# ------------------------  Sitemap plugin settings  -----------------------
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'weekly'
    }
}
			