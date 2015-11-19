'''
Created on Aug 11, 2015

@author: agp
'''
from math import floor
from queue import Queue

def searchInAdjacentElements(adjacentElements,elem):
    '''find index of an elem in an array (adjacentElements) 
    of numbers that change +1 or -1, return -1 if it doesn't exist''' 
    elementsLen=len(adjacentElements)
    i=0
    if elementsLen == 0:
        return -1
    while i<elementsLen:
        if elem == adjacentElements[i]:
            #print(i)
            return i
        i=i+abs(adjacentElements[i]-elem)
    return -1
def findIntersectionBetweenSortedArrays(array1,array2):
    """accepts two sorted arrays, 
    returns another array of the common elements"""
    intersection=[]
    j=0
    i=0
    array2len=len(array2)
    array1len=len(array1)
    if array2len == 0 or array1len == 0:
        #print(intersection)
        return intersection
    while i<array1len and j<array2len:
        if array1[i]==array2[j]:
            intersection.append(array1[i])
            j=j+1
            i=i+1
        elif array1[i]<array2[j]:
            i=i+1
        else:
            j=j+1
    #print(intersection)
    return intersection
def findIntersectionBetweenUnsortedArrays(array1,array2):
    intersection=[]
    elementDic={i:0 for i in array1+array2}
    for i in array1:
        elementDic[i]=elementDic[i]+1
    for j in array2:
        if elementDic[j]>0:
            intersection.append(j)
            elementDic[j]=elementDic[j]-1
    #print(elementDic)
    return intersection
def calculateComplexity(n):
    """(n-1)(n-2)+(n-2)(n-3)+..2.1"""
    suM=0
    for i in range(0,n-1):
        suM+=i*i+1
    return suM
"""for n in range(0,1000):
    cn=calculateComplexity(n)
    print("%d:%d:%d"%(n,cn,n**3/(cn+1)))""" # O(n**3)
def findTriplets_inefficient(integerList,n):
    """return a list of all triplet indices in the 
    integerList where the real elements sum to zero, O(n**3)"""    
    length=len(integerList)
    triplets=[]
    for i in range(0,length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if i!=j and j!=k and i!=k:
                    if integerList[i]+integerList[j]+integerList[k]==n:
                        triplets.append([i,j,k])                        
    return triplets
def insertIntoPair(elementPair,i):
    '''get sorted elementPair, insert i in a sorted way
     and return the triplet'''
    triple=[]
    if i>elementPair[0]:
        triple=[i]+elementPair
    elif i>elementPair[1]:
        triple=[elementPair[0],i,elementPair[1]]
    else:
        triple=elementPair+[i]
    return triple
def mergeIntoTriplets(tripletDict,pairs,i): 
    """add pairs+i triplet to the triplet dictionary in a unique way"""   
    for j in pairs:
        if j[0] !=i and j[1]!=i:
            value=insertIntoPair(j,i) #sorted insertion           
            tripletDict[str(value)]=value 
            
def findTriplets(integerList,n):
    """return a list of all triplet indices in the 
    integerList where the real elements sum to n, O(n**2)"""
    triplets={}
    for i,j in enumerate(integerList):
        mergeIntoTriplets(triplets,findPairs(integerList,n-j),i)
    return list(triplets.values())
def findPairs(integerList,n):
    """return a list of all pairs' indices in the 
    integerList where the real elements sum to n"""
    pairs=[]
    indices={i:[] for i in integerList}
    j=0
    #create a dictionary of value:indexList
    for i in integerList:
        indices[i].append(j)
        j+=1
    j=0
    for i in integerList:
        m=indices.get(n-i)
        if m!=None:
            for k in m:
                if k>j:
                    pairs.append([k,j])
        j+=1
    return pairs
#print(findPairs([3,2,-1,1,-2,4,-3,-4,0,5,0,0], 0))
#print(findPairs([0,0,0,0,0,0,0], 0))
#print(findTriplets([0,0,0,0],0))
def countingSort(integerList,maxVal):
    """sort/replace an array with small maxVal"""
    sortedArray=[0 for i in range(0,maxVal+1)]#O(n)
    for j in integerList:
        sortedArray[j]+=1
    k=0
    for i in range(0,maxVal+1):#O(maxVal)
        for j in range(0,sortedArray[i]):
            integerList[k]=i
            k+=1            
    return integerList
def findMax(integerList):
    """integerList must be nonempty"""
    maxim=integerList[0]
    for i in integerList:
        if maxim < i:
            maxim=i
    return maxim
def findNumberOfDigits(n):
    '''find number of digits in n in an efficient way'''
    r=1 
    n=abs(n)
    while n>=10000000000000000:
        n//=10000000000000000
        r+=16
    while n>=100000000:
        n//=100000000
        r+=8
    while n>=100:
        n//=100
        r+=2
    while n>=10:
        n//=10
        r+=1
    return r

def radixSort(integerList,ascending=True):
    '''my radix sort implementation'''
    if len(integerList)==0:
        return []
    maxNumDigits=findNumberOfDigits(findMax(integerList))    
    buckets=[Queue() for i in range(0,10)]
    k=1
    for _ in range(0,maxNumDigits):        
        for i in integerList:
            buckets[(i//k)%10].put_nowait(i)
        m=0
        if ascending:
            for i in buckets:
                while not i.empty():
                    integerList[m]=i.get_nowait()
                    m+=1
        else:#descending order
            for i in buckets[::-1]:
                while not i.empty():
                    integerList[m]=i.get_nowait()
                    m+=1
        k*=10
    return integerList
#print(countingSort([0,1,1,1,9,12,239,3,1,1,0,7,8],239))
#print(radixSort([0,1,1,1,9,12,239,3,1,1,0,7,8]))
#print(radixSort([11110,1,1,1,9,12,239,3,1,1113,0,7,8]))
#print(radixSort([0,1,1,1,9,12,239,3,1,1,101101,73232,18]))
#print(radixSort([0,1,13232,1,9,123,239,3,1,1,0,7,8],ascending=False))

def zeroSubArrays(integerList):
    """return all sub arrays that sums to zero"""    
    if len(integerList)==0:
        return [[]]
    j=0
    cumulativeSum=0
    sumList=[i for i in integerList]
    # construct a cumulative array
    for i in sumList:
        cumulativeSum+=i
        sumList[j]=cumulativeSum
        j+=1
    #print(sumList)
    """if there are duplicate elements
    indices of them are the range of the zero sum
    e.g. sumArray[i]=sumArray[j], -> [i+1,j] 0,1""" 
    # construct a dictionary key = cumulative sum, val=[i1,i2]
    ranges={}
    j=0
    zeroSums=[]
    for i in sumList:
        if ranges.get(i) == None:
            ranges[i]=[j]            
        else:
            for k in ranges[i]:
                zeroSums.append([k,j])
            ranges[i].append(j)
        if i == 0:
            zeroSums.append([j,j])
        j+=1
    return zeroSums    

def minDiffSubArrays(integerList):
    """return two sub arrays with minimum difference"""
    cumulativeSum=integerList.copy()
    j=0
    csum=0
    for i in cumulativeSum:
        csum+=i
        cumulativeSum[j]=csum
        j+=1
    j=0
    indexTable={i:[] for i in cumulativeSum}
    for i in cumulativeSum:
        indexTable[i].append(j)
        j+=1
    sorted(indexTable.items())
minDiffSubArrays([0,1,2,3,-1,-1,-2,-3,-4,-5,1,2,6,-10,1])
#momo=[[1,2],[3,4],[5,6],[7,8]]
#print(momo[:])
#print(momo[:][:])
def countInversions1(integerList):
    """inversion: integerList[i]>integerList[j] where i <j"""
    ctr=0
    marked=False
    for (i,j) in zip(integerList,sorted(integerList)):
        if i!=j:
            marked=True
            ctr+=1
        elif marked:
            ctr+=1
    return ctr
def countInversions(integerList):
    """inversion: integerList[i]>integerList[j] where i <j"""
    global ctr
    ctr=0
    def splitAndMerge(left,right):
        '''get left and right, further split them, 
        and then merge them using mergeArrayWithCount'''
        l=left
        r=right        
        if len(left)>1:
            l=splitAndMerge(left[:floor(len(left)/2)], left[floor(len(left)/2):])
        if len(right)>1:
            r=splitAndMerge(right[:floor(len(right)/2)], right[floor(len(right)/2):])
        return mergeArrayWithCount(l,r)
    def mergeArrayWithCount(left,right):
        '''count the inversions in two arrays and merge them'''
        global ctr
        merged=[]
        if len(right)==0:
            return left
        j=0
        i=0
        while i <len(left):
            if j>= len(right) or right[j]>= left[i]:
                merged.append(left[i])
                i+=1
            else:
                while j< len(right) and right[j]< left[i]:
                    ctr+=1
                    merged.append(right[j])
                    j+=1
        while j<len(right): # if there are still elements remained
            merged.append(right[j])
            j+=1
        return merged
    splitAndMerge(integerList[:floor(len(integerList)/2)],integerList[floor(len(integerList)/2):])
    return ctr    

#print(zeroSubArrays([0,1,1,2,-2,-2,0,0,-1,2,3,4,5,-9,10]))

### real amazon question :)
#int [N][N]maze
#0 -> open path
#1 -> wall 
#2 -> goal

#int start_x, start_y

#maze[i][j] == 1 -> wall
#global solution_path
#global stop
solution_path=[]

stop=0
maze=[[0,0,1,0],
      [0,0,1,0],
      [0,0,0,0],
      [0,1,2,0]]
def goToEmptyDirections(maze,x,y,path):
    '''search the maze recursively by marking the
    visited parts with findPath'''
    if x+1<len(maze[:][y]):
        if maze[x+1][y]==0 or maze[x+1][y]==2:
            findPath(maze,x+1,y,path)
    if y+1<len(maze[x][:]):
        if maze[x][y+1]==0 or maze[x][y+1]==2:
            findPath(maze,x,y+1,path)
    if x-1>=0:
        if maze[x-1][y]==0 or maze[x-1][y]==2:
            findPath(maze,x-1,y,path)
    if y-1>=0:
        if maze[x][y-1]==0 or maze[x][y-1]==2:
            findPath(maze,x,y-1,path)

#findPath(maze, 0, 0, [])
#print(solution_path)
def findPath(maze,x,y,path):
    global stop
    global solution_path
    """find a path from starting position to goal in a maze represented by 
    two dimensional array 0=free,1=wall,2=goal, simple solution that doesn't find
    the shortest path""" 
    new_path= path.copy()
    if stop == 1:
        return
    if maze[x][y]  == 2:
        path.append([x,y])
        stop=1
        solution_path=path
    else:        
        new_path.append([x,y])
        maze[x][y]=3
        goToEmptyDirections(maze,x,y,new_path)
def findShortestPath(maze,x,y):
    """find a shortest path from starting position (x,y) to goal in a maze"""
    if len(maze)<1:
        return []
    goal=breadthFirstExplore(maze, x, y)
    if goal == None:
        print("No solution path exists")
        return []
    return findAShortestPath(maze,goal[0],goal[1],x,y)
def findAShortestPath(maze,x,y,x0,y0):
    '''find one possible shortest path in a maze, that's been already explored
    and marked by the breadthFirstExplore function'''
    val=getMazeValue(maze, x, y)
    if x==x0 and y==y0:
        #maze[x][y]+=1  making it the absolute max
        return [(x,y)]
    a=getMazeValue(maze, x+1, y)
    b=getMazeValue(maze, x, y+1)
    c=getMazeValue(maze, x-1, y)
    d=getMazeValue(maze, x, y-1)        
    direction=max(a,b,c,d,val)
    if direction==a:
        return findAShortestPath(maze, x+1, y, x0, y0)+[(x,y)]
    if direction==b:
        return findAShortestPath(maze, x, y+1, x0, y0)+[(x,y)]
    if direction==c:
        return findAShortestPath(maze, x-1, y, x0, y0)+[(x,y)]
    if direction==d:
        return findAShortestPath(maze, x, y-1, x0, y0)+[(x,y)]
    return []

def getMazeValue(maze,x,y):
    '''assume that invalid x,y values points to a wall'''
    if len(maze)==0:
        return 1
    if x<0 or y<0:
        return 1
    elif x>=len(maze) or y>=len(maze[0][:]):
        return 1
    else: 
        return maze[x][y]
def breadthFirstExplore(maze,x,y):
    '''explore a maze in a breadth first manner'''
    qLen=len(maze[0][:])*len(maze)
    pointQueue=Queue(qLen)
    pointQueue.put_nowait((x,y,qLen))
    goal=None
    maze[x][y]=qLen
    while not pointQueue.empty():
        i=pointQueue.get_nowait()
        x=i[0]
        y=i[1]
        k=i[2]
        val=getMazeValue(maze, x, y)
        if val==2:
            goal=(x,y)
            return goal
        else:
            maze[x][y]=k
        #explore the neighborhood
        a=getMazeValue(maze, x+1, y)
        b=getMazeValue(maze, x, y+1)
        c=getMazeValue(maze, x-1, y)
        d=getMazeValue(maze, x, y-1)
        if a==0 or a ==2:
            pointQueue.put((x+1,y,k-1))
        if b==0 or b==2:
            pointQueue.put((x,y+1,k-1))
        if c==0 or c==2:
            pointQueue.put((x-1,y,k-1))
        if d==0 or d==2:
            pointQueue.put((x,y-1,k-1))
    return goal  

#print("-----------------")
#print(findShortestPath(maze, 0, 0))
#print("-----------------")
"""class MazeNode:
    '''hmm, unnecessary and inefficient, no need'''
    def __init__(self,val,neighbors=[]):
        self.neighbors=neighbors
        self.val=val
    def addNeighbor(self,neighbor):
        self.neighbors.append(neighbor)
class MazeGraph(object):
    def __init__(self, maze,x,y):
        val=getMazeValue(maze, x, y)
        self.startNode=MazeNode(val)
        if val==0:
            self.explore(maze,x,y,self.startNode)
    def explore(self,maze,node,x,y,node):               
        val=getMazeValue(maze,x,y)        
        if val!=0 or val!=2:
            return
        if val==2:      
        left=getMazeValue(maze,x,y-1)
        node.left=MazeNode(left)
        self.explore(maze,x,y-1,node.left)
        if left==0 or left==2:
            leftNode=[x,y-1,left,self.explore(maze,x,y-1),self.explore(maze,x,y+1),self.explore(maze,x-1,y),self.explore(x+1,y)]
        else:
            leftNode=None
        right=getMazeValue(maze,x,y+1)
        up=getMazeValue(maze,x-1,y)
        down=getMazeValue(maze,x+1,y)            
        if val==0 or val==2:  
            self.startNode=[x,y,val,leftNode,rightNode,upNode,downNode] 
        return MazeNode(val,leftNode,rightNode,upNode,downNode)
    pass"""


