#s={}
#print(type(s))                 #output=dict

#s={2,42,5,25,2,5,2,55}
#print(type(s))                  #output=set

#s={2,42,5,25,2,5,2,55}  
#print(s)                        #output={2,5,55,25,42}

'''
add
update
remove
pop
'''
#s={2,42,5,25,2,5,2,55}
#s.add(123)
#print(s)                            #output={2,42,5,25,2,5,2,55,123}     

#s={2,42,5,25,2,5,2,55}
#s.update({1,2,3})
#print(s)                             #output={1,2,3,5,55,25,42}

#s={2,42,5,25,2,5,2,55}
#s.remove(42)
#print(s)                             #output={2,5,55,25}

#s={2,42,5,25,2,5,2,55}#it will delete randomly
#s.pop()
#print(s)                                #output={5,55,25,42}     

'''set operations
union()
intersection()
difference()
issubset()
issuperset()
''' 

#union means all the set operations will be performed in the output
#set1={1,2,3}
#set2={4,5,6}
#print(set1.union(set2))                     #output=1,2,3,4,5,6

#intersection means it will perform only common numbers of a output
#set1={1,2,3,4}
#set2={4,5,6}
#print(set1.intersection(set2))                #output=4

#difference same will be deleted from the set and the output will be represented only from seta
#set1={1,2,3,4}
#set2={4,5,6}
#print(set1.difference(set2))                   #output=1,2,3

#issubset means if the set2 is equal to set1 then the output is true
#set1={1,2,3,4,5,6}
#set2={4,5,6}
#print(set2.issubset(set1))                      #output=true

#issuperset means set1 elements will be in set2 elements
#set1={1,2,3}
#set2={4,5,6}
#print(set1.issuperset(set2))                       #output=false








