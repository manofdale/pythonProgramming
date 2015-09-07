'''
Created on Sep 2, 2015

@author: eon
'''
import unittest
from interviewPrepAshay.secondPhoneQuestion import segment


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.wordSet=set(['is','help','need','needed','the','boy','he','eat','ate','ice','cream'])
        self.testCases=(('theboyateicecream','the boy ate ice cream'),('',''),('mumbojumbo',''),('helpisneeded','help is needed'))
    def testSegment(self):
        for (inp,outp) in self.testCases:
            with self.subTest((inp,outp)==(inp,outp)):
                self.assertEqual(segment(inp,self.wordSet),outp)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSegment']
    unittest.main()