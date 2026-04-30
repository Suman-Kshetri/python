import json

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'skills': ['Python', 'Data Analysis', 'Machine Learning']
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)