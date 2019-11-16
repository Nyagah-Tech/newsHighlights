class Article :
    '''
    this class defines how a particular article will be made
    '''
    def __init__(self,name,author,title,urlToImage,description,publishedAt,content):
        self.name = name
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
