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
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        actions=["Go to lunch with a coworker that you're not familiar with and get to know them!",
                 "Compliment your coworkers!",
                 "During your break, walk around the office.",
                 "Organize your workspace.",
                 "Remember to sit or stand up straight and not slouch as much as you can.",
                 "Try meditating/relaxing by sitting still for 2-5 minutes during your break.",
                 "Go have an interesting conversation with your boss that is not about work.",
                 "Try to focus on your work by not using your phone/computer as much as you can.",
                 "Try reflecting on your day after work (or doing work) and evaluate your accomplishments.",
                 "Make sure to say Hello and Goodbye to your coworkers when entering and leaving the office. (bonus points for smiling while doing that)",
                 "Go home! (After you finished your work :D )",
                 "Create a to-do list with realistic goals and tasks for you to perform.",
                 "Keep track of what you do during the day. Now how much time it took for you to do the work.",
                 "Take some time to learn more about the industry that you are working in."]
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))

class MusicHandler(webapp2.RequestHandler):
    def get(self):
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
        template = JINJA_ENVIRONMENT.get_template('templates/stress.html')
        actions=['Get a massage.',
                 'Go for a run.',
                 'Pet a dog and/or a cat!',
                 'Make yourself a nice cup of tea.',
                 'Soak in a warm bath.',
                 'Listen to music. (Have you tried or music section?)',
                 'Go have a nice talk with a friend.',
                 'Talk out your problems to yourself.',
                 'Eat a nice healthy meal.',
                 'Try to read some jokes and laugh away your stress',
                 'Try keeping a stress journal where you write about your problems.',
                 'Try taking a short nap.',
                 'Try doing an arts and crafts project.']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        actions=['Make a fort out of your cushions, pillows, and blankets! (bonus points for getting friends to help you!!)',
                 'Take a nap!',
                 'Call a friend.',
                 'Try texting a good friend a message backwards (ex: "elpmaxe") and see how long it takes for them to decode the message.',
                 'Bake something for yourself and/or friends.',
                 'Plan a sleepover!',
                 'Speak only in rhymes!!',
                 'Try to find Narnia!',
                 'Have a costume Party w/ friends! (not just a Halloween activity)',
                 'Read a book! (JK Just watch a movie instead)',
                 'Watch cute cat videos on YouTube!!!!',
                 'Bake Cookies! (props for sharing them with friends)']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))

class ExerciseHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/exercise.html')
        actions=['Get a friend to be your work out parter so you can both motivate each other.',
                 'Try making yourself a protein shake!',
                 'Try playing a sport with your friends regularly so you have more motivation for working out.',
                 'If you are used to exercising in a gym try exercising outside the gym for a change or vise versa.',
                 'Try changing your exercise routine (try an early morning exercise routine or late night routine).',
                 'Make sure to do a lot of breathing!! (Seriously)',
                 'Try listening to music while exercising. (check our music section)',
                 'Try not listening to music while exercising in order to focus on your form.',
                 'Try listening/watching to a podcast or a TV show while exercising.',
                 'Try joining a workout class or an exercise group.',
                 'Challenge yourself!!!',
                 'Watch some workout motivation videos on YouTube before starting.']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class SchoolHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/school.html')
        actions=['Make a study group with your friends.',
                 'Join a new type of club!',
                 'Explore the campus.',
                 "Talk to a teacher/professor you're unfamiliar with.",
                 'Talk to a new student.',
                 'Try high fiving one of your friends when they raise their hand to ask a question.',
                 'Try getting a head start on the next lesson in class. (nerd.. Jk!)',
                 'Ask as many questions as you can think (relating to the lesson) to your teacher.',
                 'Try writting weekly schedules of what you have to do.',
                 'Try doodling on your notes when you can, but still pay attention to the lesson.']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class CrazyHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/crazy.html')
        actions=['Go skydiving!',
                 'Take a hike.',
                 'Climb a mountain.',
                 'Swim with dolphins.',
                 'Go bungee jumping!',
                 'Do something crazy!!',
                 'If your brave, try doing Shark cage diving.',
                 'Go run on the Great Wall of China!!',
                 'Start a conversation with a random person! (and be nice!!)',
                 'Go to a concert and be determined to meet the artist.'
                 'Go see the Great Pyramid of Giza!',
                 'Dress up nice for no reason at all!',
                 'Fly a kite??',
                 'Go to the zoo!!!',
                 'Take regular photos of yourself (possibly every day) for a year, and then watch how you changed!',
                 'Watch Adam Sandler movies!!!']
        self.response.write(template.render({"phrase":actions[random.randint(0,len(actions)-1)]}))


class ChillHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/chill.html')
        actions=['Read a book.',
                 'Watch something on Netflix! (or Hulu or Amazon)',
                 'Get some ice (ba-dum-tss).',
                 'Go watch a movie.',
                 'Do yoga.',
                 'Eat some Ice Cream!! (frozen yogurt is also acceptable)',
                 'If you can, try and ride a swing!',
                 'Take a nap.',
                 'Calmy ride a bike.',
                 'Try experimenting with food in the kitchen.',
                 'Go fishing.',
                 'Go relax on a beach.',
                 'Bowling??']
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
