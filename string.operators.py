a= 'Hello'
b= 'Ram'

print(a+' '+b) #concatenation
print(a*2) #repetition

c='apple,ball,cat'
d= c.split(',')
print(d) #['apple', 'ball', 'cat']

e= ','.join(d)
print(e) #apple,ball,cat

print(f'Reverse of {a} is {a[::-1]}')
print(a[0]) #Indexing
print(a[-1]) #Last letter
print(a[1:3]) #Slicing

print('H' in a) #Membership Test
print('H' not in a) #Non-membership test

print(a.startswith('J')) #False
print(a.endswith('o')) #True

print(a.isalpha()) #True
print(a.isdigit()) #False
print(' '.isspace()) #True
print('abc123'.isalnum()) #True

print(a.count('l')) #2
print(a.index('l')) #index of the first 'l'
print(len(a)) #length of a

print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.title())

p= '   Hello World!    '
print(p.strip()) #removes empty space before and after the string

