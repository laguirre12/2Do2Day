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
                 "Try meditating/relaxing by sitting still for 2-5 minutes during your break.",]
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        self.post()

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/music.html')
        actions=['Start singing for fun!',
                 'Try to learn how to play an instrument.']
        num=random.randint(0,10)
        if not (num==0 or num==1):
            genres=open("genre_file.txt","r")
            list_genres=[]
            for line in genres:
                list_genres.append(line)
            num2=random.randint(0,len(list_genres)-1)
            logging.info(list_genres[num2])
            try:
                self.response.write(template.render({
                "phrase": 'Listen to ' +list_genres[num2]+" music!"
                }))
            except:
                self.response.write(template.render({
                "phrase": 'Listen to J-Pop'+" music!"
                }))
        else:
            self.response.write(template.render({"phrase":actions[num]}))

class StressHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/stress.html')
        actions=['Get a massage.',
                 'Go for a run.',
                 'Pet a dog and/or a cat!',
                 'Make yourself a nice cup of tea.',
                 'Soak in a warm bath.']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        actions=['Make a fort out of your cushions, pillows, and blankets!',
                 'Take a nap!',
                 'Call a friend.',
                 'Bake something for yourself and/or friends.',
                 'Plan a sleepover!']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))

class ExerciseHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/exercise.html')
        actions=['Get a friend to be your work out parter so you can both motivate each other.',
                 'Try making yourself a protein shake!',
                 'Try playing a sport with your friends regularly so you have more motivation for working out.',
                 'If you are used to exercising in a gym try exercising outside the gym for a change or vise versa.',
                 'Try changing your exercise routine (try an early morning exercise routine or late night routine).']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class SchoolHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/school.html')
        actions=['Make a study group with your friends.',
                 'Join a new type of club!',
                 'Explore the campus.',
                 "Talk to a teacher/professor you're unfamiliar with",
                 'Talk to a new student.']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class CrazyHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/crazy.html')
        actions=['Go skydiving!',
                 'Take a hike.',
                 'Climb a mountain.',
                 'Swim with dolphins.',
                 'Go bungee jumping!']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class ChillHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/chill.html')
        actions=['Read a book.',
                 'Watch something on Netflix.',
                 'Get some ice (ba-dum-tss).',
                 'Go watch a movie.',
                 'Do yoga.']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


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
