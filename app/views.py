from flask import render_template
from app import app
from .request import get_newsSource

#views
@app.route('/')
def index():
    '''
    this is a view function thats responsible for returning the index page and its data
    '''
    title = " The News Highlight apllication "

    #getting the news-sources
    news_sources = get_newsSource('sources')
    print(news_sources)


    return render_template('index.html',title = title,srcNews = news_sources)

@app.route('/newsSrc/<int:source_id>')
def newSource(source_id):
    '''
    this view function returns the news articles that are in particular news source
    '''
    render_template('Newsource.html', id = source_id)
    