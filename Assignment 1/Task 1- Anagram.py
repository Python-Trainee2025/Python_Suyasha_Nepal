# Take input from user for two words, and check if they are anagrams

word1= list(input('Enter first word: '))
word2= list(input('Enter second word: '))

w1_lower= [x.lower() for x in word1]
w2_lower= [x.lower() for x in word2]

w1_lower.sort()
w2_lower.sort()

print("The two words are anagrams." if w1_lower==w2_lower else "The two words are not anagrams.")
