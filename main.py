import os
import webapp2
import jinja2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class WorkHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        self.response.write(template.render({"phrase":"eventually send in"}))

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/music.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/music.html')
        self.response.write(template.render({"phrase":"eventually send in"}))

class StressHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/stress.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/stress.html')
        self.response.write(template.render({"phrase":"eventually send in"}))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render({"phrase":"eventually send in"}))

class ExerciseHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/exercise.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/exercise.html')
        self.response.write(template.render({"phrase":"eventually send in"}))


class SchoolHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/school.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/school.html')
        self.response.write(template.render({"phrase":"eventually send in"}))


class CrazyHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/crazy.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/crazy.html')
        self.response.write(template.render({"phrase":"eventually send in"}))


class ChillHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/chill.html')
        self.response.write(template.render({"phrase":"eventually send in"}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/chill.html')
        self.response.write(template.render({"phrase":"eventually send in"}))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/work',WorkHandler),
    ('/music',MusicHandler),
    ('/stress',StressHandler),
    ('/home',HomeHandler),
    ('/exercise',ExerciseHandler),
    ('/school',SchoolHandler),
    ('/crazy',CrazyHandler),
    ('/chill',ChillHandler)
], debug=True)
