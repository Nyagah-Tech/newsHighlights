from flask import render_template,url_for
from . import main 
from ..request import get_newsSource,get_sourceArticle,top_head

#views
@main.route('/')
def index():
    '''
    this is a view function thats responsible for returning the index page and its data
    '''
    title = " The News Highlight application "

    #getting the news-sources
    top_headline = top_head('business')
    news_sources = get_newsSource('sources')
    print(news_sources)


    return render_template( 'index.html',title = title,topHeads = top_headline,srcNews = news_sources)

@main.route('/articles/<source_id>')
def sourceArticles(source_id):
    '''
    this view function returns the news articles that are in particular news source
    '''
    articles = get_sourceArticle(source_id)
    title = "The News Articles "
    print(articles)

    return render_template('articles.html', title = title, articles = articles)
    