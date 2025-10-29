# Read a text file and count the number of words in it.
# Handle the case where the file might not exist.

# file= open("words.txt", "w")
# file.write("This is a dummy sentence.\n This is a dummy sentence.\n")
# file.close()

f_name = str(input("Enter text file name: "))

try:
    with open(f_name) as f:
        words = f.read().split()
        print(f"{f_name} has {len(words)} words.")

except FileNotFoundError:
    print(f"{f_name} does not exist.")