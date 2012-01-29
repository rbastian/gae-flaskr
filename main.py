__author__ = 'rbastian'

from google.appengine.ext.webapp.util import run_wsgi_app
from game import app

run_wsgi_app(app)