#Data types batate hain ki hum memory mein kis tarah ka data store kar rahe hain.
#Numerical: int, float
#int: Whole numbers (e.g., 5, -10).
#float: Decimal numbers (e.g., 3.14, -2.0).
#Feature: Python handles arbitrarily large integers automatically.

a=10  ## integer
print(type(a))
b=10.5 ## Float
print(type(b))

#############################################################################################################

#String (str)
#Textual data. Python mein strings "immutable" (change nahi ho sakti) hoti hain.
#Slicing: s[0:5] (shuru ke 5 chars).
#Methods: .upper(), .lower(), .strip(), .replace().

c="Jamshaid Basit,Hunter"
print(c[0:4])
print(c.upper())  ## UPPER CASE
print(c.lower())  ##lower case
print(c.strip(","))  ## Remove Whitening space and stripes
print(c.replace("a","e"))  ## Replace a with e in Name
print(c.replace("a","e",2))  ## Replace a with e in Name and 2 is number of times it replace

##########################################################################################################
#List (The Versatile One)
#Ordered, mutable (changeable), and allows duplicates.
#Features: append(), extend(), insert(), pop(), remove(), sort().
list1=[1,2,3,4]
list1.append(10)
print(list1)
list2=[2,4,6,8]
list1.extend(list2)  #iterable	Required. Any iterable (list, set, tuple, etc.)
print(list1)
list1.pop(1)  ##Remove item from indexing  it will remov eitem on index 1 at this point
print(list1)
list1.remove(1)  ## Remove item from list  , here it will remove 1 from item 
print(list1)
list1.sort()  ## Sorting Small to large
print(list1)
list1.sort(reverse=True)  ## Sorting Large to Small
print(list1)

###################################################################################################
##Tuple (The Constant One)
##Ordered but immutable. Once created, cannot be changed. Fast performance.
##Use case: Coordinates, database records.

## Tuples(Immutable as String)
tup=(1,2,3,4)
print(tup)
print(tup[1:3])  ## Range same as List 
#tup[0]=10  ## Error not allowed
tup=()  ## Empty Tuples
tup=(1)  ## It work as integeter not tuples
tup=(1,)  ## Single Tuples  
print(tup)   
##Tuple Methods
print(tup.index(1))  ## Indexing of Tuple
print(tup.count(1))  ## Occurant integer in tuples

#########################################################################################################
#Dictionary (dict - Hashmap)
#Key-Value pairs. Unordered (Python 3.7+ mein ordered insertion maintain hoti hai), mutable.
#Features: keys(), values(), items(), get().
user = {"name": "Ali", "age": 25}
print(user)
print(user["name"])
print(user.keys())  ## find keys from given dictionaries
print(user.values())  ## values of dictionaries
print(user.items())   ## complete vocabulary items
print(user.get("age"))

########################################################################################################3
#Set
#Unordered collection of unique elements.
#Use case: Duplicates hatane ke liye.
#Features: union(), intersection(), difference().
set1={1,2,4,5,7,7}
set2={2,4,5,6}
print(type(set1))
print(set1.union(set1))   ## union between set1 and set2 
print(set1.intersection(set2))  ## intersection between set1 and set2
print(set1.difference(set2))   ## diference between set1 and set2

###########################################################################################################


