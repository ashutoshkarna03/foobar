import  unittest
from foobar import FoobarClass 
 
 
class FooBarTest(unittest.TestCase):
 
    def setUp(self):
 
        self.foo = FoobarClass()

    def test_read_data(self):
        self.foo.code_map = {}

        self.assertEqual(list,type(self.foo.read_data()))

    def test_compute_score(self):
        self.foo.max_score=0

        self.assertEqual(list,type(self.foo.compute_score()))







if __name__=='__main__':
    unittest.main()
