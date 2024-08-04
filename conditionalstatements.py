#if
#ifelse
#elif
#nestedif

'''
syntax : 
if condition:
   statements
elif:
    statements
else:
   statements
'''

#if True:
    #print("nenu if")
#elif True:
    #print("nenu elif")
#else:
    #print("nenu else")     #output: nenu if

#if False:
    #print("nenu if")
#elif True:
    #print("nenu elif")
#else:
    #print("nenu else")       #output: nenu elif

#if False:
    #print("nenu if")
#elif False:
    #print("nenu elif")
#else:
    #print("nenu else")        #output: nenu else

#nested if
if True:
    print("inner if")
    if True:
        print("outer if")
    else:
        print("inner if")
else:
       print("outer if")        #output : inner if and outer if

#if False:
    #print("inner if")
    #if True:
        #print("outer if")
    #else:
        #print("outer if")
#else:
    # print("inner if")               #output : inner if


#age=18
#if age>18:
    #print("you can vote")
#elif age==18:
    #print("yes you can vote")
#else:
    #print("wait")    # output : yes you can vote                  
    

