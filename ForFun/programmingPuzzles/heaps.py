'''
Created on Aug 25, 2015

@author: eon
'''
class MyHeap(object):
    '''
    classdocs
    '''
    def __init__(self, heapSize=0,elementList=[],branching=2,compare=lambda x,y: x<y):
        '''
        Constructor
        '''
        self.elementList=elementList        
        self.configure(heapSize,branching,compare)
    def configure(self,heapSize=0,branching=2,compare=lambda x,y: x<=y):
        self.heapSize=heapSize 
        #limitLength        
        self.compare=compare # heap condition, min heap default        
        self.branching=branching
        self.buildHeap()
    def getParentIndex(self,i):
        '''return -1 if i==0'''
        return ((i-1)//self.branching)
    def getBoundedIndex(self,i):
        '''return either i or max index available according to heap size'''
        if self.heapSize==0:
            return i
        if i>=self.heapSize:
            return self.heapSize-1
        return i
    def getChildrenRange(self,i):
        '''return the index range of children in the array'''
        minIndex=i*self.branching+1
        maxIndex=(i+1)*self.branching
        return (self.getBoundedIndex(minIndex),self.getBoundedIndex(maxIndex))
    def swapElements(self,i,j):
        temp=self.elementList[j]
        self.elementList[j]=self.elementList[i]
        self.elementList[i]=temp
    def heapify(self,i):
        '''assuming that children nodes maintain heap property, 
        fix the overall heap property rooted at i'''
        #check the children first
        (first,last)=self.getChildrenRange(i)
        newParent=i
        for j in range(first,last+1):#check below
            if not self.compare(self.elementList[i],self.elementList[j]):
                if not self.compare(self.elementList[newParent],self.elementList[j]):
                    newParent=j # find the best candidate for a parent
        
        if i!=newParent:#swap i with the new parent
            self.swapElements(newParent, i)
            self.heapify(newParent)        
    def buildHeap(self):
        if self.heapSize==0:
            lim=self.heapSize//2
        else:
            lim=len(self.elementList)
        for i in range(min(len(self.elementList)//2,lim),0,-1):
            self.heapify(i)
    def addWithReplacement(self,element):
        '''good for keeping k=heapSize number of largest or smallest elements'''
        if len(self.elementList)==0:
            self.elementList.append(element)
        elif self.heapSize!=0 and len(self.elementList)>=self.heapSize:
            if not self.compare(element,self.peek()):#else do not add
                self.elementList[0]=element
                self.heapify(0)
        else:
            self.insert(element)
    def insert(self,element):
        '''insert an element into the heap disregarding the heap size'''
        self.elementList.append(element)
        i=len(self.elementList)-1
        while i>0:
            j=self.getParentIndex(i)
            if not self.compare(self.elementList[j],element):#if not heap property
                self.swapElements(i, j)
                i=j
            else: 
                break
    def pop(self):
        lastElement=self.removeLast()
        if len(self.elementList)==0:
            return lastElement
        firstElement=self.elementList[0]
        self.elementList[0]=lastElement
        self.heapify(0)
        return firstElement
    def removeLast(self):
        return self.elementList.pop()
    def getIterator(self):
        return self.elementList
    def peek(self):
        '''do not peek an empty heap, use getSize first'''
        return self.elementList[0]
    def getSize(self):
        return len(self.elementList)


         





"""def heapify(self,i):#max or min
        '''assuming that the tree is a heap, heapify it when entry i changed'''
        if i>self.heapSize:
            print("error, element is out of range i > heap size")
            return
        elif i==self.heapSize:
            minRemove=True
        else:
            while True:
                j=self.getParentIndex(i)
                if reduce(self.elementList[]self.getChildren,self.compare)
                if j <0:
                    break            
                if not self.compare(self.elementList[j],self.elementList[i]):
                    #swap
                    temp=self.elementList[j]
                    self.elementList[j]=self.elementList[i]
                    self.elementList[i]=temp
                    i=j
                else:
                    break
        if minRemove:
            self.pop()#maintain the heap size
        return i
        #if i==newParent:#no check above
        #    pass
            #j=self.getParentIndex(i)
            #if j>0 and not self.compare(self.elementList[j],self.elementList[i]):#then swap                
            #    self.swapElements(i, j)
        """