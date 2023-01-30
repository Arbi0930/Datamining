#lab 1.1

x = 4              
print(x, type(x))

y = True           
print(y, type(y))

z = 3.7            
print(z, type(z))

s = "Стринг өгөгдөл: фуцж гэсэн утга авна"    
print(s, type(s))

#lab 1.2

x = 4            
x1 = x + 4        
x2 = x * 3       
x += 2           
x3 = x       
x *= 3           
x4 = x      
x5 = x % 4       

z = 3.7          
z1 = z - 2       
z2 = z / 3      
z3 = z // 3      
z4 = z ** 2      
z5 = z4 ** 0.5   
z6 = pow(z,2)    
z7 = round(z)    
z8 = int(z)      

print(x,x1,x2,x3,x4,x5)
print(z,z1,z2,z3,z4)
print(z5,z6,z7,z8)


#lab 1.3

import math
x = 4
print(math.sqrt(x))      
print(math.pow(x,2))     
print(math.exp(x))       
print(math.log(x,2))     
print(math.fabs(-4))     
print(math.factorial(x)) 

z = 0.2
print(math.ceil(z))      
print(math.floor(z))     
print(math.trunc(z))     

z = 3*math.pi           
print(math.sin(z))      
print(math.tanh(z))     

x = math.nan            
print(math.isnan(x))


x = math.inf            

print(math.isinf(x))

#lab 1.4
y1 = True
y2 = False

print(y1 and y2)       
print(y1 or y2)        
print(y1 and not y2)   

#lab 1.5

s1 = "This"
print(s1[1:])                    
print(len(s1))                               
print("Length of string is " + str(len(s1))) 
print(s1.upper())                          
print(s1.lower())                            

s2 = "This is a string"
words = s2.split(' ')             
print(words[0])
print(s2.replace('a','another'))  
print(s2.replace('is','at'))      
print(s2.find("a"))               
print(s1 in s2)                   

print(s1 == 'This')            
print(s1 < 'That')                
print(s2 + " too")                
print((s1 + " ")* 3) 

#lab 1.5

intlist = [1, 3, 5, 7, 9]
print(type(intlist))
print(intlist)
intlist2 = list(range(0,10,2))   # range[startvalue, endvalue, stepsize]
print(intlist2)

print(intlist[2])                # get the third element of the list
print(intlist[:2])               # get the first two elements
print(intlist[2:])               # get the last three elements of the list
print(len(intlist))              # get the number of elements in the list
print(sum(intlist))              # sums up elements of the list

intlist.append(11)               # insert 11 to end of the list
print(intlist)
print(intlist.pop())             # remove last element of the list
print(intlist)
print(intlist + [11,13,15])      # concatenate two lists
print(intlist * 3)               # replicate the list
intlist.insert(2,4)              # insert item 4 at index 2  
print(intlist)
intlist.sort(reverse=True)       # sort elements in descending order
print(intlist)

#lab1.6
mylist = ['this', 'is', 'a', 'list']
print(mylist)
print(type(mylist))

print("list" in mylist)          # check whether "list" is in mylist
print(mylist[2])                 # show the 3rd element of the list
print(mylist[:2])                # show the first two elements of the list
print(mylist[2:])                # show the last two elements of the list
mylist.append("too")             # insert element to end of the list

separator = " "
print(separator.join(mylist))    # merge all elements of the list into a string

mylist.remove("is")              # remove element from list
print(mylist)

#lab1.7

abbrev = {}
abbrev['MI'] = "Michigan"
abbrev['MN'] = "Minnesota"
abbrev['TX'] = "Texas"
abbrev['CA'] = "California"

print(abbrev)
print(abbrev.keys())            # get the keys of the dictionary
print(abbrev.values())          # get the values of the dictionary
print(len(abbrev))              # get number of key-value pairs

print(abbrev.get('MI'))
print("FL" in abbrev)
print("CA" in abbrev)

keys = ['apples', 'oranges', 'bananas', 'cherries']
values = [3, 4, 2, 10]
fruits = dict(zip(keys, values))
print(fruits)
print(sorted(fruits))     # sort keys of dictionary

from operator import itemgetter
print(sorted(fruits.items(), key=itemgetter(0)))    # sort by key of dictionary
print(sorted(fruits.items(), key=itemgetter(1))) 

#lab1.8

MItuple = ('MI', 'Michigan', 'Lansing')
CAtuple = ('CA', 'California', 'Sacramento')
TXtuple = ('TX', 'Texas', 'Austin')

print(MItuple)
print(MItuple[1:])

states = [MItuple, CAtuple, TXtuple]    # this will create a list of tuples
print(states)
print(states[2])
print(states[2][:])
print(states[2][1:])

states.sort(key=lambda state: state[2])  # sort the states by their capital cities
print(states)

#lab1.9

x = 10

if x % 2 == 0:
    print("x =", x, "is even")
else:
    print("x =", x, "is odd")

if x > 0:
    print("x =", x, "is positive")
elif x < 0:
    print("x =", x, "is negative")
else:
    print("x =", x, "is neither positive nor negative")


#lab 1.10

mylist = ['this', 'is', 'a', 'list']
for word in mylist:
    print(word.replace("is", "at"))
    
mylist2 = [len(word) for word in mylist]   # number of characters in each word
print(mylist2)

# using for loop with list of tuples

states = [('MI', 'Michigan', 'Lansing'),('CA', 'California', 'Sacramento'),
          ('TX', 'Texas', 'Austin')]

sorted_capitals = [state[2] for state in states]
sorted_capitals.sort()
print(sorted_capitals)

# using for loop with dictionary

fruits = {'apples': 3, 'oranges': 4, 'bananas': 2, 'cherries': 10}
fruitnames = [k for (k,v) in fruits.items()]
print(fruitnames)

#lab1.11
mylist = list(range(-10,10))
print(mylist)

i = 0
while (mylist[i] < 0):
    i = i + 1
    
print("First non-negative number:", mylist[i])

#lab1.12
myfunc = lambda x: 3*x**2 - 2*x + 3      

print(myfunc(2))

#lab1.13
import math

# The following function will discard missing values from a list
def discard(inlist, sortFlag=False):    # default value for sortFlag is False 
    outlist = []
    for item in inlist:
        if not math.isnan(item):
            outlist.append(item)
            
    if sortFlag:
        outlist.sort()
    return outlist

mylist = [12, math.nan, 23, -11, 45, math.nan, 71]

print(discard(mylist,True))   
#lab1.14
states = [('MI', 'Michigan', 'Lansing'),('CA', 'California', 'Sacramento'),
          ('TX', 'Texas', 'Austin'), ('MN', 'Minnesota', 'St Paul')]

with open('states.txt', 'w') as f:
    f.write('\n'.join('%s,%s,%s' % state for state in states))
    
with open('states.txt', 'r') as f:
    for line in f:
        fields = line.split(sep=',')    # split each line into its respective fields
        print('State=',fields[1],'(',fields[0],')','Capital:', fields[2])