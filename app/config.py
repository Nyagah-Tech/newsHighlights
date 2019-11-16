class Config:
    '''NEWS_API_BASE_URL 
    this are general configuration for the parent class
    '''

    = 'https://newsapi.org/v2/{}?apiKey={}'

    pass

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