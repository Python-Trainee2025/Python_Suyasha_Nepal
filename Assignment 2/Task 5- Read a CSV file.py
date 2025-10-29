# Read a .csv file and print each row.
# Handle file not found and other parsing errors if needed

import csv

f_name = input("Enter csv file name: ")

try:
    with open(f_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("No such file or directory.")


except csv.Error as e:
    print("CSV parsing error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)
