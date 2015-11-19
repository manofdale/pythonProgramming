'''
Created on Jul 26, 2015

@author: agp
'''
import unittest
from programmingPuzzles.linkedList import LinkedList


class Test(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    '''def testInit(self):
        linked=LinkedList([0]);
        #linked.printContents()
        #print()
        pass'''
    def testReverse(self):
        linked=LinkedList([0,1,2,3]);
        linked.reverse()
        #linked.printContents()        
        #print(" odo,".strip(' ,')+"mellburn"[::-1])
        self.assertEqual(linked.returnList(),[3,2,1,0],"not reversed")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReverseLinkedList']
    unittest.main()
