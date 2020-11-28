import  unittest
from foobar import FoobarClass 
 
 
class FooBarTest(unittest.TestCase):
 
    def setUp(self):
 
        self.foo = FoobarClass()

    def test_read_data(self):

        # check for empty dictionary 

        self.foo.code_map = {}
        self.assertEqual(list,type(self.foo.read_data()))

        # check for different data type (list, str, int) 
        self.foo.code_map = 0
        self.assertEqual([],self.foo.read_data())

        self.foo.code_map =''
        self.assertEqual([],self.foo.read_data())

        self.foo.code_map = []
        self.assertEqual([],self.foo.read_data())

    def test_compute_score(self):

        # check for zero divison 

        self.foo.max_score=0
        self.assertEqual(list,type(self.foo.compute_score()))

        # check for different data type (list, str, int) 

        self.foo.max_score=''
        self.assertEqual(list,type(self.foo.compute_score()))

        self.foo.max_score={}
        self.assertEqual(list,type(self.foo.compute_score()))








if __name__=='__main__':
    unittest.main()
