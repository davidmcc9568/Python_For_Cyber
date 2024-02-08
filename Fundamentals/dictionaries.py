# dictionaries

# 'key':value 

person = {
    'name': 'David',
    'job': 'Student',
    'age': 50,
    'is_employed': True,
    'hobbies': ['jogging', 'eating', 'gaming']
}

#printing a value from an embedded list in a dictionary 
# print(person['hobbies'][0])

#dictionaries nested in a list
people = [{'name': 'David'}, {'name': 'Josh'}, {'name': 'Brenda'}]
for person in people:
    print(person['name'])

