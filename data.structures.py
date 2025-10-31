###########LIST###########
'''
enclosed in square brackets
values separated by comma
ordered
can have duplicates
mutable
[1, 2, 3]
'''

a= [1, 2, 3, 8, 3, 9, 10]

print(a[0]) #Indexing
print(a[-1]) #Negative indexing
print(a[0:3]) #Slicing, start: end-1
print(a[::-1]) #Reversing
print(len(a)) #Length
print(a.index(3)) #Index of the first occurrence of 3 in the list

a.reverse() #Modifies a
print(a)

a.append(10)
print(a)

a.insert(4, 100) #Inserts 100 at index 4
print(a)

print(a.count(3)) #list method, counts the number of occurrences of 3

# a.sort() #modifies a
# print(a)

x= sorted(a) #doesn't modify a
print(x)

l1= ["apple", "banana", "orange"]
l2= ["cat", "dog", "rabbit"]

# List Operations
print(l1+l2) #Concatenation
print(l1*2) #Repetition
print("apple" in l1) #Membership Test

a.remove(10) #removes the first occurrence of 10
print(a)

del(a[3]) #deletes the element at index 3
print(a)

popped= a.pop(6) #pops the element at index 6 and assigns it to 'popped'
print(popped)

a[2]= 7 #replaces the value index 2 with 7

a.clear() #removes all elements from a

#List input
l_ip= input("Enter values separated by space: ").split(' ')
print(l_ip)

###########TUPLE###########
'''
ordered
can have duplicates
immutable
(1, 2, 2, 3)
accessing elements (including slicing, and reversal) and index, 
concat, repetition, checking membership, count, length, similar to that of lists
'''

tuple_with_a_single_element= (2, ) #requires a comma

p= 1, 2, 3 #tuple packing
l, m, n= p #tuple unpacking

nested_tuple= ((4, 5, 6), (7, 8, 9))
print(nested_tuple[0][1]) #accessing elements in a nested tuple

#DICTIONARY
'''
{key:value}
unordered
mutable
{'a':1, 'b':2}
'''
d = {'a': 1, 'b': 2, 'c': 3}

print(d.keys())  # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

e= dict(s=1, t= 4, u= 'a')
print(e)

print(e['s']) #accessing values of keys
e['i']= 2 #adding new values  to a dictionary

del e['t']  #removing values
e.pop('s') #removes key 's'

e.popitem() #removes the last inserted item

q1 = {'a': "apple", 'b': "ball"}
q2 = {'y': "yellow", 'z': "zebra"}

q1.update(q2) #key-value pairs in q1 are appended in q2, existing keys are replaced
print(q1)

print('y' in q1) #membership test

#Iteration
for key, value in q1.items():
    print(key, value)

#Nested dictionary
emp_info= {
    "employee1": {'name': "Ram", 'role': "Trainee"},
    "employee2": {'name': "John", 'role': "Manager"},
}

print(emp_info['employee1']['name']) #accessing elements in a nested dictionary

emp_copy= emp_info.copy()  #copying a dictionary

keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0) #dictionary with default values
print(default_dict)  # values of all keys= 0

print(q1.get('a'), "a")  # If 'a' is not found, it returns None (and not an error)
print(q1.get('x', 'Not Found')) # If 'x' is not found,it returns "Not Found" (default value) and not an error or None


# Dictionary Comprehension
squared = {x: x**2 for x in range(1, 6)}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25

#SET
'''
mutable
no duplicates allowed, which separates it from lists
unordered
{1,2,3}
'''

empty_set= set() # {}

s= {1, 7, 6, 5}

s.add(9) #adding an element
s.remove(1) #removing an element
s.discard(2) #like remove, but no error if 2 is not present
s.clear() #remove all elements
print(len(s)) #set length


# Set Operations
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)  # Union
print(s1.union(s2))  # Alternative for union

print(s1 & s2)  # Intersection
print(s1.intersection(s2))  # Alternative for intersection

print(s1 - s2)  # Difference
print(s1.difference(s2))  # Alternative for difference

print(s1 ^ s2)  # Symmetric Difference: intersecting values are removed
print(s1.symmetric_difference(s2))  # Alternative for symmetric difference

# Check membership like in lists

# Subset and Superset Checks
s3 = {1, 2}
print(s3.issubset(s1))  # True (s3 is subset of s1)
print(s1.issuperset(s3))  # True (s1 is superset of s3)


s4 = s1.copy() #copying a set

# Frozen Sets (Immutable Sets)
f_set = frozenset([1, 2, 3, 4])
print(f_set)
