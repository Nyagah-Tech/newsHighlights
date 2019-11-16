from app import app
import urllib.request,json
from .models import newSource
NewSrc = newSource.NewSrc

#fetching the api key
api_key = app.config['NEWS_API_KEY']
# fetching the news base url
base_url = app.config['NEWS_API_BASE_URL']

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

        source_object = NewSrc(name,description,category,url)
        newsSource_results.append(source_object)

    return newsSource_results




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