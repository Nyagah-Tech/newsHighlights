from app import app
import urllib.request,json
from .models import article
from .models import newSource
NewSrc = newSource.NewSrc
NewArticle = article.Article

#fetching the api key
api_key = app.config['NEWS_API_KEY']
# fetching the news base url
base_url = app.config['NEWS_API_BASE_URL']

articles_url = app.config['NEWS_ARTICLES_API']
top_url = app.config['TOP_URL']

def process_sources(source_list):
    '''
    this function will process the newsSource list into objects
    Args:
        source_list: this is a list of dictionaries that contains news sources details that have been given by the url

        returns: it return a list of news sources list

    '''

    newsSource_results=[]
    for newssource in source_list:
        name = newssource.get('name')
        description = newssource.get('description')
        category = newssource.get('category')
        url = newssource.get('url')
        id = newssource.get('id')

        source_object = NewSrc(name,description,category,url,id)
        newsSource_results.append(source_object)

    return newsSource_results

def process_articles(articleList):
    '''
    this function will process the articles list into objects
    Args:
        artcleList: this is a list of dictionaries that contains news articles of a particular news source

        return: it returns a list of allnew sources list
    '''
    articles_results=[]
    for article in articleList:
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        urlToImage = article.get('urlToImage')
        description = article.get('description')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        url = article.get('url')

        article_object = NewArticle(name,author,title,urlToImage,description,publishedAt,content,url)
        articles_results.append(article_object)
    
    return articles_results



def get_newsSource(category):
    '''
    this is a function that fetches the json respone from the url
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        newsSource_results = None

        if get_source_response['sources']:
            newsSource_list = get_source_response['sources']
            newsSource_results = process_sources(newsSource_list)

    return newsSource_results


def get_sourceArticle(id):
    '''
    this function will display all the articles in a particular source
    '''
    get_srcArticles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_srcArticles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_list = None

        if articles_response['articles']:
            articles_list = articles_response['articles']
            articles_results = process_articles(articles_list)

    return articles_results

def top_head(category):
    get_top_url = top_url.format(category,api_key)

    with urllib.request.urlopen(get_top_url) as url:
        top_hds_data = url.read()
        top_hds_response = json.loads(top_hds_data)

        tops_lists = None

        if top_hds_response['articles']:
            tops_lists = top_hds_response['articles']
            top_headlines = process_articles(tops_lists)
            
    return top_headlines
