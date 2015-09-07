'''
Created on Jul 26, 2015

@author: eon
'''
class Node(object):
        '''
        classdocs
        '''
        def __init__(self,nodElement=None,nextElement=None):
            self.element=nodElement
            self.next=nextElement
        
class LinkedList(object):
    '''
    classdocs
    '''


    def __init__(self, listElems=None):
        '''
        Constructor
        '''
        self.constructFromList(listElems)
    def constructFromList(self,listElems):
        if len(listElems) >0:
            self.head=Node(listElems[0])
        else:
            self.head=None
            self.tail=None
            return
        currentNode=self.head
        for i in listElems[1:]:
            node=Node(i)
            currentNode.next=node
            currentNode=node
        currentNode.next=None
        self.tail=currentNode
        return
    def deleteAll(self):
        self.head=None
        self.tail=None
        # anything else?
    def reverse(self):
        listElems=self.returnList()
        self.deleteAll()
        self.constructFromList(listElems[::-1])
        
    def addElement(self,node):
        if node is None:
            return False
        node=Node(node)
        self.tail.next=node
        self.tail=node
        self.tail.next=None
        return True
    def deleteElement(self,node):
        if node is None:
            return False
        curr=self.head
        if curr.element is node:
            self.head=curr.next
            return True
        while curr.next != None:
            if curr.next.element is node:
                if curr.next.next is None:
                    self.tail=curr
                curr.next=curr.next.next
                return True
        return False
    def printContents(self):
        print(self.returnList())  
    def returnList(self):
        arrayVersion=[]
        curr=self.head
        while curr != None:
            arrayVersion.append(curr.element)
            curr=curr.next
        return arrayVersion    