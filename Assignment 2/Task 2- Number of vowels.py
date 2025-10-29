# Accept a word/sentence from the user and count how many vowels are present in it.

sentence= list(input("Enter a sentence: ").split(' '))
# print(sentence)

lower_sentence = [x.lower() for x in sentence]
# print(lower_sentence)

count= 0

characters= []

for i in lower_sentence:
    for j in i:
        characters.append(j)

# print(characters)

for i in characters:
    if i in 'a' or i in 'e' or i in 'i' or i in 'o' or i in 'u':
        count+=1

print(f"There are {count} vowels in the sentence.")