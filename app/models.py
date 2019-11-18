class Article :
    '''
    this class defines how a particular article will be made
    '''
    def __init__(self,name,author,title,urlToImage,description,publishedAt,content,url):
        self.name = name
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url


class NewSrc:
    '''
    this is a News source class that defines the sources object.how they will be created
    '''
    def __init__(self,name,description,category,url,id):
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        self.id = id
