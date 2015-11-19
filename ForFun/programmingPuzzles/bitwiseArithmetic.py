'''
Created on Aug 9, 2015

@author: agp
'''
from math import floor, log2
def addWithoutPlus1(a,b):
    if b==0:
        return a
    if b>=2<<64:
        return a^(-2<<64)
    x=a^b
    c=(a&b)<<1
    print([x,c])    
    return addWithoutPlus(x,c)
def addWithoutPlus(a,b):
    while b!=0:
        if b>=2<<64:
            return a^(-2<<64)
        c=a&b
        a=a^b
        b=c<<1
    return a
def negate(a):
    return addWithoutPlus(~a,1)
"""
x & 1             == x%2
x & (1<<n)        get the nth bit
x | (1<<n)        set the nth bit
x& ~(1<<n)        unset the nth bit
x ^ (1<<n)        toggle it
x & (x-1)         turn off the rightmost bit: 110&(110-1)=100
x & (-x)          isolate the rightmost bit: 110 & (-110 = ~100+1 = 10)=10
x | (x-1)         right propagate the rightmost bit: 101000|(101000-1)=101111
~x & (x+1)        isolate the rightmost zero bit: ~11011 & (11011+1)=100
x | (x+1)         set the rightmost zero bit: 10011&(10011+1)=10111
xor temp trick needs equality check: a^=b b^=a a^=b
"""
def reverseBitSeq(n,bitlen): # inefficient and unnecessarily complex
    if bitlen==1:
        return n
    half_bitlen=floor(bitlen/2)
    leftHalf=n>>half_bitlen
    middleMask=1<<(half_bitlen)
    rightHalf=n&(middleMask-1)
    if bitlen%2==1:#reverseBitSeq(left,half_bitlen),1,reverseBitseq(rightHalf,half_bitlen)
        middleBit=n&middleMask
        leftHalf=leftHalf>>1
        return (reverseBitSeq(rightHalf, half_bitlen)<<(half_bitlen+1)) | middleBit | reverseBitSeq(leftHalf, half_bitlen)
    else:#reverseBitSeq(left,bitlen/2),reverseBitseq(right,bitlen/2)
        return (reverseBitSeq(rightHalf, half_bitlen)<<(half_bitlen)) | reverseBitSeq(leftHalf, half_bitlen)
def reverseBitSeq1(n):
    r=0
    while r == 0 and n>2:#skip the trailing zeroes        
        r=n%2
        n=n>>1
    while n>=1:#reverse the rest
        r=(r<<1)+n%2
        n=n>>1
    return r
def isPalindrom(n):
    while n%2==0:
        n=n>>1
        if n == 0:
            return True
    return reverseBitSeq1(n)==n
def isPalindrom1(n):
    while n&1==0:
        n>>=1
        if n<2:
            return True
    bitlen=floor(log2(n))+1
    leftMask=1<<(bitlen-1)
    rightMask=1
    while leftMask>rightMask:
        if (n&leftMask>0 and n&rightMask>0) or (n&leftMask==0 and n&rightMask ==0):
            pass
        else:
            return False
        leftMask>>=1
        rightMask<<=1
    return True
