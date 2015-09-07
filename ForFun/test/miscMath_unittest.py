'''
Created on Aug 9, 2015

@author: eon
'''
import unittest
from programmingPuzzles.miscMath import generatePowerSet
from programmingPuzzles.bitwiseArithmetic import addWithoutPlus,negate,reverseBitSeq,reverseBitSeq1, isPalindrom,isPalindrom1
from programmingPuzzles.miscMath import findSmallestK,find007,\
    countTheTrailingZerosOfFactorial
from programmingPuzzles.arrays import countInversions


class Test(unittest.TestCase):

    def test_generatePowerSet(self):
        self.assertEqual(generatePowerSet([]),[])
        self.assertEqual(generatePowerSet([1]),[[],[1]])
        self.assertEqual(generatePowerSet([1,2]),[[],[1],[2],[1,2]])
    def test_addWithoutPlus(self):
        self.assertEqual(addWithoutPlus(1523,12), 1535)
        self.assertEqual(addWithoutPlus(0,1), 1)
        self.assertEqual(addWithoutPlus(0,0), 0)
        self.assertEqual(addWithoutPlus(-1,1), 0)
        self.assertEqual(addWithoutPlus(-11523,12), -11511)
    def test_negate(self):
        self.assertEqual(negate(1), -1)
        self.assertEqual(negate(103), -103)
        self.assertEqual(negate(-15), 15)
        self.assertEqual(negate(0), 0)
    def test_findSmallestK(self):
        self.assertEqual(findSmallestK(729),999)
        self.assertEqual(findSmallestK(9),9)
        self.assertEqual(findSmallestK(-729),999)
        self.assertEqual(findSmallestK(1453),-1)
        self.assertEqual(findSmallestK(-19),-1)
        self.assertEqual(findSmallestK(0),0)
    def test_find007(self):
        self.assertEqual(find007(2590259),7770777)
        self.assertEqual(find007(23569023569),70707070707)
        self.assertEqual(find007(11),77)
        self.assertEqual(find007(10),70)
    def test_countTheTrailingZerosOfFactorial(self):
        self.assertEqual(countTheTrailingZerosOfFactorial(5), 1)
        self.assertEqual(countTheTrailingZerosOfFactorial(4), 0)
        self.assertEqual(countTheTrailingZerosOfFactorial(-1), 0)
        self.assertEqual(countTheTrailingZerosOfFactorial(10), 2)
        self.assertEqual(countTheTrailingZerosOfFactorial(15), 3)
    def test_reverseBitSeq(self):
        self.assertEqual(reverseBitSeq(0b1010110,7), 0b0110101)
        self.assertEqual(reverseBitSeq(0,1), 0)
        self.assertEqual(reverseBitSeq(0b1,1), 0b1)
        self.assertEqual(bin(reverseBitSeq(0b101011011101,12)), bin(0b101110110101))
    def test_reverseBitSeq1(self):
        self.assertEqual(reverseBitSeq1(0b1010110), 0b0110101)
        self.assertEqual(reverseBitSeq1(0), 0)
        self.assertEqual(reverseBitSeq1(0b1), 0b1)
        self.assertEqual(bin(reverseBitSeq1(0b101011011101)), bin(0b101110110101))
    def test_isPalindrom(self):
        self.assertTrue(isPalindrom(0b1))
        self.assertTrue(isPalindrom(0))
        self.assertTrue(isPalindrom(0b1010101))
        self.assertTrue(isPalindrom(0b011001100110))
        self.assertFalse(isPalindrom(0b10110))
    def test_isPalindrom1(self):
        self.assertTrue(isPalindrom1(0b1))
        self.assertTrue(isPalindrom1(0))
        self.assertTrue(isPalindrom1(0b1010101))
        self.assertTrue(isPalindrom1(0b111001100111))
        self.assertTrue(isPalindrom1(0b011001100110))
        self.assertFalse(isPalindrom1(0b10110))
    @unittest.skip("")
    def test_countInversions(self):
        self.assertEqual(countInversions([]), 0)
        self.assertEqual(countInversions([5,6,4]), 2)
        self.assertEqual(countInversions([6,5,4]), 3)
        self.assertEqual(countInversions([1,2,5,6,4,3,7,8]), 4)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()