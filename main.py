import os
import webapp2
import jinja2
import random
import logging
from google.appengine.ext import ndb

_actions=[]
_actions.append(["Go to lunch with a coworker that you're not familiar with and get to know them!",
         "Compliment your coworkers!",
         "During your break, walk around the office. (slowly)",
         "Organize your workspace.",
         "Remember to sit or stand up straight and not slouch as much as you can! (that's an order)",
         "Try meditating/relaxing by sitting still for 2-5 minutes during your break.",
         "Go have an interesting conversation with your boss that is not about work.",
         "Try to focus on your work by not using your phone/computer as much as you can.",
         "Try reflecting on your day after work (or doing work) and evaluate your accomplishments.",
         "Go home! (After you finish your work :D )",
         "Create a to-do list with realistic goals and tasks for you to perform.",
         "Keep track of what you do during the day and know how much time it took for you to do that work.",
         "Take some time to learn more about the industry that you are working in."])

_actions.append(['Start singing for fun!',
         'Try to learn how to play an instrument!'])

_actions.append(['Get a massage.',
                 'Go for a run.',
                 'Pet a dog and/or a cat!',
                 'Make yourself a nice cup of tea.',
                 'Soak in a warm bath.',
                 'Listen to music! (Have you tried our music section?)',
                 'Go have a nice talk with a friend.',
                 'Talk out your problems to yourself.',
                 'Eat a nice healthy meal.',
                 'Read some jokes and laugh away your stress.',
                 'Try keeping a stress journal where you write about your problems.',
                 'Take a short nap.',
                 'Do an arts and crafts project!'])
_actions.append(['Make a fort out of your cushions, pillows, and blankets! (bonus points for getting friends to help you!!)',
         'Take a nap!',
         'Call a friend.',
         'Text a good friend a message backwards (ex: "elpmaxe") and see how long it takes for them to decode the message.',
         'Bake something for yourself and/or friends.',
         'Plan a sleepover!',
         'Speak only in rhymes!!',
         'Find Narnia!',
         'Have a costume party with friends! (not just a Halloween activity)',
         'Read a book! (JK watch a movie instead)',
         'Watch cute cat videos on ',
         'Bake Cookies! (props for sharing them with friends)'])
_actions.append(['Get a friend to be your work out parter so you can both motivate each other.',
         'Make yourself a protein shake!',
         'Try playing a sport with your friends regularly so you have more motivation for working out.',
         'If you are used to exercising in a gym, try exercising outside the gym for a change (or vise versa).',
         'Try changing your exercise routine (try an early morning exercise routine or late night routine).',
         'Make sure to do a lot of breathing!! (Seriously)',
         'Listen to different music while exercising. (check our music section)',
         'Try not listening to music while exercising in order to focus on your form.',
         'Join a workout class or an exercise group.',
         'Watch some workout motivation videos on '])
_actions.append(['Make a study group with your friends.',
         'Join a new type of club!',
         'Explore the campus.',
         "Talk to a teacher/professor you're unfamiliar with.",
         'Talk to a new student.',
         'High five one of your friends when they raise their hand to ask a question.',
         'Try getting a head start on the next lesson in class. (be a nerd!)',
         'Write weekly schedules of what you have to do.',
         'Doodle on your notes. Become an artist.'])
_actions.append(['Go skydiving!',
         'Go on a hike.',
         'Climb a mountain.',
         'Swim with dolphins.',
         'Go bungee jumping!',
         "If you're brave, try Shark cage diving.",
         'Go run on the Great Wall of China!!',
         'Start a conversation with a random person! (and be nice!!)',
         'Go to a concert and be determined to meet the artist.',
         'Go see the Great Pyramid of Giza!',
         'Dress up nice for no reason at all!',
         'Fly a kite??',
         'Go to the zoo!!!',
         'Take regular photos of yourself (possibly every day) for a year, and then watch how you changed!',
         'Watch Adam Sandler movies!!!'])

_actions.append(['Read a book.',
         'Watch something on Netflix! (or Hulu, Amazon, HBO, etc.)',
         'Get some ice (ba-dum-tss).',
         'Go watch a movie.',
         'Do yoga.',
         'Eat some ice cream!! (frozen yogurt is also acceptable)',
         'Go on a swing!',
         'Take a nap.',
         'Ride a bike.',
         'Try experimenting with food in the kitchen.',
         'Go fishing.',
         'Go relax on a beach.',
         'Bowling??'])

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class WorkHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        self.response.write(template.render({"phrase":_actions[0][random.randint(0,len(_actions[0])-1)]}))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[0].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion")}))

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/music.html')
        num=random.randint(0,10)
        logging.info(num)
        if num>3:
            genres=open("genre_file.txt","r")
            list_genres=[]
            for line in genres:
                list_genres.append(line)
            num2=random.randint(0,len(list_genres)-1)
            try:
                self.response.write(template.render({
                "phrase": 'Listen to ' +list_genres[num2]+" music!","number":num
                }))
            except:
                self.response.write(template.render({
                "phrase": 'Listen to J-Pop'+" music!","number":num
                }))
        else:
            self.response.write(template.render({"phrase":_actions[1][random.randint(0,len(_actions[1])-1)],"number":0}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/music.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[1].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion"),"number":0}))

class StressHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/stress.html')
        self.response.write(template.render({"phrase":_actions[2][random.randint(0,len(_actions[2])-1)]}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/stress.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[2].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion")}))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render({"phrase":_actions[3][random.randint(0,len(_actions[3])-1)]}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[3].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion")}))

class ExerciseHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/exercise.html')
        self.response.write(template.render({"phrase":_actions[4][random.randint(0,len(_actions[4])-1)]}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/exercise.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[4].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion")}))


class SchoolHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/school.html')
        self.response.write(template.render({"phrase":_actions[5][random.randint(0,len(_actions[5])-1)]}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/school.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[5].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion")}))


class CrazyHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/crazy.html')
        self.response.write(template.render({"phrase":_actions[6][random.randint(0,len(_actions[6])-1)]}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/crazy.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[6].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion")}))


class ChillHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/chill.html')
        self.response.write(template.render({"phrase":_actions[7][random.randint(0,len(_actions[7])-1)]}))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/chill.html')
        if ("{" in self.request.get("suggestion") or self.request.get("suggestion")=="" or self.request.get("suggestion").isspace() or "*" in self.request.get("suggestion") or "<" in self.request.get("suggestion")
            or ">" in self.request.get("suggestion") or "@" in self.request.get("suggestion") or "}" in self.request.get("suggestion") ):
            self.get();
        else:
            _actions[7].append(self.request.get("suggestion"))
            self.response.write(template.render({"phrase":self.request.get("suggestion").strip()}))

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
