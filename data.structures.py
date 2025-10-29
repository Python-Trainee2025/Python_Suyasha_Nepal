#LIST
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

a.reverse() #Modifies a
print(a)

a.append(10)
print(a)

a.insert(4, 100) #Inserts 100 at index 4
print(a)

print(a.count(3)) #counts the number of occurences of 3

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

#TUPLE
'''
ordered
can have duplicates
immutable
(1, 2, 2, 3)
'''

#DICTIONARY
'''
{key:value}
unordered
mutable
{'a':1, 'b':2}
'''

#SET
'''
mutable
no duplicates allowed, which separates it from lists
unordered
{1,2,3}
'''