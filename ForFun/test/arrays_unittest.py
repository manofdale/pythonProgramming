'''
Created on Aug 25, 2015

@author: agp
'''
import unittest
from programmingPuzzles.arrays import findTriplets,\
    findIntersectionBetweenSortedArrays, findIntersectionBetweenUnsortedArrays
from programmingPuzzles.arrays import searchInAdjacentElements

def stringify(numberList):#uniquely reorder a random list of sorted lists
    strList=[]
    for i in numberList:
        strList.append(str(i))        
    return sorted(strList)

class Test(unittest.TestCase):
    def testTripletSum(self):
        """find all triplets of numbers such that a[i]+a[j]+a[k]=N"""
        
        self.assertEqual(stringify(findTriplets([0,1,2,-1,0,0],0)),stringify([[3,1,0],[5,4,0], [4, 3, 1], [5, 3, 1]]))
        self.assertEqual(findTriplets([],0),[])
        self.assertEqual(stringify(findTriplets([0,0,0,0], 0)), stringify([[2,1,0],[3,1,0],[3,2,0],[3,2,1]]))
    def testSearchInAdjacentElements(self):
        self.assertEqual(searchInAdjacentElements([0,1,0,-1,0,1,2,3,4,3,4,3,4,3,4,5,6,7,8,9,10,9],10),20)
    def testFindIntersectionBetweenSortedArrays(self):
        self.assertEqual([], findIntersectionBetweenSortedArrays([], []), "both empty fails")
        self.assertEqual([], findIntersectionBetweenSortedArrays([], [1,2,3]), "left empty fails")
        self.assertEqual([], findIntersectionBetweenSortedArrays([1,2,3], []), "right empty arrays fail")
        self.assertEqual([1], findIntersectionBetweenSortedArrays([1,2,3], [1,1]), "right shorter fail")
        self.assertEqual([1], findIntersectionBetweenSortedArrays([1,1],[1,2,3]), "left shorter fail")
        self.assertEqual([1,1,2,4,6], findIntersectionBetweenSortedArrays([1,1,1,2,3,4,5,6,6], [1,1,2,4,4,6]), "duplicates fail")
        self.assertEqual([3,5,678],findIntersectionBetweenSortedArrays([1,2,3,4,5,6,7,11,134,678],[3,5,111,555,678,19999]))
    def testFindIntersectionBetweenUnsortedArrays(self):
        self.assertEqual([], findIntersectionBetweenUnsortedArrays([], []), "both empty fails")
        self.assertEqual([], findIntersectionBetweenUnsortedArrays([], [1,2,3]), "left empty fails")
        self.assertEqual([], findIntersectionBetweenUnsortedArrays([1,2,3], []), "right empty arrays fail")
        self.assertEqual([1], findIntersectionBetweenUnsortedArrays([3,1,2], [1,1]), "right shorter fail")
        self.assertEqual([1], findIntersectionBetweenUnsortedArrays([1,1],[2,1,3]), "left shorter fail")
        self.assertEqual(sorted([1,1,2,4,6]), sorted(findIntersectionBetweenUnsortedArrays([1,2,1,3,1,4,6,5,6], [6,1,4,2,4,1])), "duplicates fail")
        self.assertEqual(sorted([3,5,678,1]),sorted(findIntersectionBetweenUnsortedArrays([678,2,6,5,4,7,11,134,3,1],[111,5,3,555,1000,678,19999,1])))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTripletSum']
    unittest.main()
