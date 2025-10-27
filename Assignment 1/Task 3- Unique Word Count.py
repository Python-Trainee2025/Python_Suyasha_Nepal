# Input a sentence or a paragraph from user and extract how many unique words are used and display the count

para= list(input("Enter a sentence or a paragraph:\n").split(' '))
# print(para)

lowercased_para= [x.lower() for x in para]
# print(lower_para)

clean_para= []

for i in lowercased_para:
    if i[-1]== '.':
        i= i[:-1]
    # print(i)
    clean_para.append(i)

# print(clean_para)

set_para= set(clean_para)
# print(set_para)

print(f"There are {len(set_para)} unique words in the paragraph.")