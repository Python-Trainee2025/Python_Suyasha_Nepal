# Get input from user and check if it is palindrome

word= input('Enter word: ')
reverse_word= word[::-1]
print(f"{word} is a palindrome word." if word.lower()==reverse_word.lower() else f"{word} is not a palindrome word.")