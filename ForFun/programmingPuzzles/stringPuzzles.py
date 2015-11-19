'''
Created on Sep 2, 2015

@author: agp
'''

#x1 = "theboyateicecream"
#x2 = "helpisneeded"
#dictionary of words
#y =  "the boy ate ice cream"
#y = segment(x, dict)
#x
#w+segment(x',knownWord)

MAX_WORD_LENGTH=100
def segment(x,knownWords):
    '''if  there is a known word in x, put a space after it, x has no space, x always makes sense'''    
    n=len(x)
    for j in range(0,n):
        if j>MAX_WORD_LENGTH:
            return ''
        if x[0:j+1] in knownWords:
            if j==n-1:
                return x # the whole word
            remainder=segment(x[j+1:],knownWords)
            if remainder!='':
                return x[0:j+1]+' '+remainder
    return ''        
        
