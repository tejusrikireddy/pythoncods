'''
list
'''
#list is denoted in square brackets[]

#v=[]
#print(type(v))            #output : list

# passing elements into the list

#v=[1,24,1,4,1544,5,'kiran']
#print (v[3])                   #output : 4

#v=[1,24,1,4,1544,5,'kiran']
#print(v[-1])                    #output : kiran



#slicing     start:stop:skip
#v=[1,24,1,4,1544,5,'kiran']
#print(v[0:4:2])                 #output = [1,1]

'''
append
extend
count
insert
pop
remove
index
'''
#v=[1,24,1,4,1544,5,'kiran']
#v.append("python")
#print(v)                 #output : v=[1,24,1,4,1544,5,'kiran','python]

#v=[1,24,1,4,1544,5,'kiran']
#v.extend([5,7,6,4,3,'teju'])
#print(v)                    #output : v=[1,24,1,4,1544,5,'kiran',5,7,6,4,3,'teju']

#v=[1,24,1,4,1544,5,'kiran']
#print[v.count(1)]            #output : 2

#v=[1,24,1,4,1544,5,'kiran']
#v.remove(24)
#print(v)                       #output : [1,1,4,1544,'kiran]

#v=[1,24,1,4,1544,5,'kiran']
#v.pop(1)
#print(v)                        #output : [1,1,4,1544,'kiran]

#v=[1,24,1,4,1544,5,'kiran']
#v.insert(0,"xyz")
#print(v)                         #output : ['xyz',1,24,1,4,1544,5,'kiran']

#v=[1,24,1,4,1544,5,'kiran']
#print(v.index(24))                 #output : 1
                  














