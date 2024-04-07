my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair

# Removing Elements:
del my_dict['city']  # Removing a key-value pair

# Checking Key Existence:
if 'age' in my_dict:
    print('Age is present in the dictionary')

# Iterating Through Keys and Values:
for key, value in my_dict.items():
    print(key, value)
