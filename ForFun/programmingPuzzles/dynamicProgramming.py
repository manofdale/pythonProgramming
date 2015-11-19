'''
Created on Sep 6, 2015

@author: agp
'''
#TODO more

def checkHalfSum(numList):
    '''Check if there exists, non-contiguous subset in array such that sum of subset is exactly 
total_sum/2. Where total_sum  = sum of all elements in array.'''    
    numSum=0
    for i in numList:
        numSum+=i
    numSumDict={}
    return hasSum(numList,0,numSum/2,numSumDict)
def hasSum(numList,k,numSum,numSumDict):
    '''return True if numList has a subset that sums up to numSum'''
    if numSumDict.get((k,numSum))!=None:
        return numSumDict[(k,numSum)]
    if len(numList)==0:
        if numSum!=0:
            return False
        else:            
            return True
    if numSum==numList[0]:
        return True
    numSumDict[(k+1,numSum-numList[0])]=hasSum(numList[1:],k+1,numSum-numList[0],numSumDict)
    numSumDict[(k+1,numSum)]= hasSum(numList[1:],k+1,numSum,numSumDict)
    numSumDict[(k,numSum)]=numSumDict[(k+1,numSum)] or numSumDict[(k+1,numSum-numList[0])]
    return numSumDict[(k,numSum)]

