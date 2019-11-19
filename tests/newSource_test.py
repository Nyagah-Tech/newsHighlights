import unittest
from .models import NewSrc,Articles
NewSrc = newSource.NewSrc

class newSrc_test(unittest.TestCase):
    '''
    test the newSrc behaviour
    '''

    def setUp(self):
        '''
        this method will run before every testcase starts
        '''
        self.new_source = NewSrc('ABC News','this is your trusted source of news','general','https://abcnews.go.com')

    def test_instance(self):
        '''
        checks if the new object created is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_source,NewSrc))

    def testnewsource_init(self):
        self.assertTrue(self.new_source.name,'ABC News')
        self.assertTrue(self.new_source.description,'this is your trusted source of news')
        self.assertTrue(self.new_source.category,'general')
        self.assertTrue(self.new_source.url,'https://abcnews.go.com')
        self.assertTrue(self.new_source.id,'id')
class article_test(uittest,Testcase):
    '''
    test the Articles behaviour
    '''
    def setUp(self):
        '''
        this will run before every article testcase
        '''
        self.new_article = Article('juma','fanda','deadly kill','https://abcnews.go.com','the description','date','content at','htpps://url')

    def testArticle_init(self):
        self.assertTrue(self.new_article.name,'juma')
        self.assertTrue(self.new_article.author,'fanda')
        self.assertTrue(self.new_article.title,'deadly kill')
        self.assertTrue(self.new_article.urlToImage,'https://abcnews.go.com')
        self.assertTrue(self.new_article.description,'the description')
        self.assertTrue(self.new_article.publishedAt,'date')
        self.assertTrue(self.new_article.content,'content at')
        self.assertTrue(self.new_article.url,'htpps://url')
if __name__ == '__main__':
    unittest.main()

