#!/usr/bin/env python
# -*- coding: utf8 -*- 

#--------------------------------------
# Edit configuration 
#

CAMINAE_SERVER = 'geobi.makina-corpus.net/ecrins-sentiers'

TITLE = {
    'en': "Trekking",
    'fr': "Portail rando",
}

DESCRIPTION = {
    'en': "Catalog of treks",
    'fr': "Offre rando",
}

GANALYTICS_TRACKING_CODE = 'UA-XXXXXXXX-XX'


#
# In development
#...................
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# LOGGING['loggers']['rando']['level'] = 'DEBUG'
# LOGGING['loggers']['']['level'] = 'DEBUG'

CACHES = {
   'default': {
       'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
       'LOCATION': 'unique-snowflake'
   }
}