'''
Created on Sep 7, 2015

@author: agp
'''
import unittest
from programmingPuzzles.dynamicProgramming import checkHalfSum


class Test(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testCases=(([0,0,0,0],True),([],True),([1,1],True),([1,2,3],True),([1,3,4],True),([1,2,3,4],True),([2,3,4],False),([1232,1,2,7,3,1200,16,3,1,5],True))


    def tearDown(self):
        pass


    def testName(self):
        for (i,j) in self.testCases:
            with self.subTest(i=i):
                self.assertEqual( checkHalfSum(i), j)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
