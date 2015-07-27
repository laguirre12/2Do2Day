import os
import webapp2
import jinja2
import random
import logging
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class WorkHandler(webapp2.RequestHandler):
    def get(self):
        self.post()

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        actions=["Go to lunch with a coworker that you're not familiar with and get to know them!",
                 "Compliment your coworkers!",
                 "During your break, walk around the office.",
                 "Organize your workspace.",
                 "Remember to sit or stand up straight and not slouch as much as you can.",
                 "Try meditating/relaxing by sitting still for 2-5 minutes during your break.",
                 ]
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        self.post()

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/music.html')
        actions=['listen to (insert artist/song here)','listen to (insert artist/song here)','listen to (insert artist/song here)','start singing for fun','try to learn how to play an instrument']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))

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
