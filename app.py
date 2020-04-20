from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/story')
def story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    story = Story([place, noun, verb, adjective, plural_noun],
                  'Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.')
    ans = {'place': place, 'noun': noun, 'verb': verb,
           'adjective': adjective, 'plural_noun': plural_noun}
    return render_template('story.html', story=story.generate(ans))

