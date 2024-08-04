#funtion means a block of a code(set of instructions)
#oka set of lines(combination of lines)
#when the function is executed : run when it is called (manam run chesinappudu execute avuthadhi)
#why functions means for the reusability(by using import)

#syntax  def function.name(){
#             function body
#          function.name() }

#example
def add(a,b):   #function definition  #a,b are parameters
    return a+b    #funcytion within a function ni nested function
print(add(1,2))  #function call       #1,2 are arguments(ivi parameters ki pampinchadam kosam 1 will go and store to a)

#nested function syntax
#def outer():
        #print ("outer")
    #def inner()
        #print ("inner")          #output: outer inner

'''
block of a code

'''
def func():     #function definition
    print("this is function")     #function body
func()      #function call                               #output:this is function


def func(a,b,c): #parameters
    print("this is function",a,b,c)
func(1,2,3)    #arguments                                            #output:this is function 1 2 3

def func(*a): #star use chesedhani manam arbitary arguments or the parameters
    print("this is function",a)
func(1,2,3)                                         #output: this is function (1, 2, 3) tuple format