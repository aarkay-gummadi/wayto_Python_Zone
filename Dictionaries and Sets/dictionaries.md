Dictionaries
------------
### Overview:
* A dictionary in Python is a data structure that allows you to store and retrieve values using keys. 
* It is also known as a hashmap or associative array in other programming languages. 
* Dictionaries are implemented as hash tables, providing fast access to values based on their keys.

### Creating a Dictionary:
```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

### Accessing Values:
```py
print(my_dict['name'])  # Output: John
```

### Modifying and Adding Elements:
```py
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
```

### Removing Elements:
```py
del my_dict['city']  # Removing a key-value pair
```

### Checking Key Existence:
```py
if 'age' in my_dict:
    print('Age is present in the dictionary')
```

### Iterating Through Keys and Values:
```py
for key, value in my_dict.items():
    print(key, value)
```   