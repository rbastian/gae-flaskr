__author__ = 'rbastian'

from google.appengine.ext import db

class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)