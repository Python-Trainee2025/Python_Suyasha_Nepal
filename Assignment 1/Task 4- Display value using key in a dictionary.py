# Create a dictionary with a person's name and contact info for a small company
# Take the input from a user to search for a user using their name, return the number

personal_info= {
    'person1': {'name':'Ram', 'contact':'4462992'},
    'person2': {'name': 'Shyam', 'contact': '4481992'},
    'person3': {'name': 'Neha', 'contact': '9876787667'},
    'person4': {'name': 'Ram', 'contact': '8877888'}
}

person= input('Enter person\'s name: ')

contact= None

# print(personal_info.items()) #list of tuples containing key-value pairs

for person_id, details in personal_info.items():
    if details['name'] == person:
        contact= details['contact']
        print(f"Contact number of {person} is: {contact}")
