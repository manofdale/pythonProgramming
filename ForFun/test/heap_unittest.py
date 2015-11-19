'''
Created on Aug 26, 2015

@author: agp
'''
import unittest
from programmingPuzzles.heaps import MyHeap


class HeapTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMinHeap(self):
        heap=MyHeap()
        self.assertEqual(heap.getSize(), 0)
        heap=MyHeap(compare=lambda x,y:x>=y)
        heap.configure(heapSize=10,compare=lambda x,y:x<=y)
        for i in range(0,100):
            heap.addWithReplacement(i)
        self.assertEqual(heap.getSize(), 10)
        self.assertEqual(heap.peek(), 90)
        #print(heap.getIterator())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
