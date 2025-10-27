# Take input from user for two words, and check if they are anagrams

word1= list(input('Enter first word: '))
word2= list(input('Enter second word: '))

word1.sort()
word2.sort()

print("The two words are anagrams." if word1==word2 else "The two words are not anagrams.")
