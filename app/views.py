from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    this is a view function thats responsible for returning the index page and its data
    '''
    return render_template('index.html')

@app.route('/newsSrc/<int:source_id>')
def newSource(source_id):
    '''
    this view function returns the news articles that are in particular news source
    '''
    render_template('Newsource.html', id = source_id)
    