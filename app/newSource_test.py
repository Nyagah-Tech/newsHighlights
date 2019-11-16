import unittest
from models import newSource
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
        self.assertTrue(isinstance(self.new_source,NewSrc))

    def testnewsource_init(self):
        self.assertTrue(self.new_source.name,'ABC News')
        self.assertTrue(self.new_source.description,'this is your trusted source of news')
        self.assertTrue(self.new_source.category,'general')
        self.assertTrue(self.new_source.url,'https://abcnews.go.com')

if __name__ == '__main__':
    unittest.main()

