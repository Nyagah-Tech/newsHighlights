import os 

class Config:
    '''
    this are general configuration for the parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?apiKey={}'
    NEWS_ARTICLES_API ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    TOP_URL ='https://newsapi.org/v2/top-headlines?category={}&apiKey={}'

    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')

class ProductionConfig(Config):
    '''
    prod configuration child class

    Args:
        Config: it inherits all the onfigurations of the parentconfig

    '''
    pass

class DevelopmentConfig(Config):
    '''
    dev configuration child class

    Args:
        Config : it inherits the parents general settings

    '''
    DEBUG = True
config_options = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}