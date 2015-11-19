'''
Created on Aug 10, 2015
@author: agp
'''
from math import floor
from random import randint

def generatePowerSet1(givenSet):
    '''return the powerset of a given set,
    e.g. [] -> [[]], [1] -> [[],[1]] etc. '''
    if len(givenSet)==0:
        return []
    #print(givenSet)
    elem=givenSet.pop()
    #print(givenSet)
    duplicate=generatePowerSet(givenSet)
    if len(duplicate)==0:
        duplicate=[[]]
    duplicate=duplicate+[i+[elem] for i in duplicate]
    #print(duplicate)
    return duplicate
def generatePowerSet(givenSet):    
    '''return the powerset of a given set,
    e.g. [] -> [[]], [1] -> [[],[1]] etc. '''
    if len(givenSet)==0:
        return []
    duplicate=[[]]
    for i in givenSet:        
        duplicate=duplicate+[j+[i] for j in duplicate]
    return duplicate

def fibonacci_inefficient(n):
    '''exponential complexity!'''
    if n==0:
        return 0
    if n==1:
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
def fibonacci(n):
    '''O(n)'''
    if n<0:
        return 0
    if n==0:
        return 0
    if n==1:
        return 1
    n_1=1
    n_2=0
    for _ in range(0,n-2):
        n_1+=n_2
        n_2=n_1-n_2
    return n_1+n_2
#for i in range(0,20):
#    print( fibonacci(i))

def rand7():
    """random generation of 7 numbers from 5 numbers"""
    vals = [[ 1, 2, 3, 4, 5 ],
        [ 6, 7, 1, 2, 3 ],
        [ 4, 5, 6, 7, 1 ],
        [ 2,  3, 4, 5, 6 ],
        [ 7, 0, 0, 0, 0 ]]
    return vals[randint(5)][randint(5)]
def getTheLeastNumber(n,k):
    """get the least number by deleting k digits"""
    digits=getDigitList(n)
    number=0    
    for i in sorted(digits)[:-k]:        
        number*=10
        number+=i
    return number
def findTheNumberOfRectangles(n):
    """how many rectangles on a chessboard of size n"""
    return ((n+1)*n/2)**2
def findTheNumberOfSquares(n):
    """how many squares on a chessboard of size n"""
    return n*(n+1)*(2*n+1)/6
def getDigitList(n):
    """convert n to a list of digits"""
    n=floor(n)
    digits=[n%10]
    n//=10
    while n>0:
        digits.append(n%10)
        n//=10
    return digits

def findSmallestK(n):
    """find the smallest number k where
    the digits in k multiply to n"""
    n=abs(n)
    if n<10:
        return n 
    digits=[]    
    while n>9:
        marked=False
        for i in range(9,1,-1):
            if n%i==0:
                n=n/i
                marked=True                
                digits.append(str(i))
                break
        if (marked == False) and n>9:
            return -1
    return int(''.join([str(int(n))]+digits[::-1]))

def find007(k):
    """find the smallest number that only has digits {0,7}
    that can be divided by k"""
    class ValueContainer(object):
        def __init__(self,val):
            self.val=val
    currentMin=ValueContainer(2<<64)
    def find07(k,n,currentMin):
        if n>=currentMin.val:
            return currentMin.val
        if n>=k and n%k==0:
            if currentMin.val>n:
                currentMin.val=n
            return n
        if n%10 == 7:
            return find07(k, n*10,currentMin)
        else:
            newMin= min (find07(k,n+7,currentMin),find07(k,n*10,currentMin))
            if currentMin.val>newMin:
                currentMin.val=newMin
            return newMin
    if k==0:
        return 0
    dodo=find07(k,7,currentMin)
    #without  passing currentMin also works
    return dodo

def countTheTrailingZerosOfFactorial1(n): #inefficient O(n)
    '''find how many trailing zeroes will be in the result of factorial'''
    zeroCount=0
    for i in range(5,n+1):
        k=i
        while k%5 ==0:
            zeroCount+=1
            k/=5
    return zeroCount
def countTheTrailingZerosOfFactorial(n): #efficient O(log5(n))    
    '''find how many trailing zeroes will be in the result of factorial'''
    k=5
    zeroCount=0
    while k<=n:
        zeroCount+=n/k
        k*=5
    return zeroCount
