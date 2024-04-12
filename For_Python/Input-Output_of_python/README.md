Output (Printing)
-------------------

### Using print() Function
* The `print()` function displays output to the console.
* Example:
```
print("Hello, World!")
```

### Formatted Output
* Use formatted string literals (f-strings) or the `.format()` method for more control over formatting.
* Example with f-string:
```
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
```

### Conversion to String
* Convert any value to a string using `str()` or `repr()` functions.
* `str()` returns human-readable representations.
* `repr()` returns representations for the interpreter.
* Example:
```
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y)
print(s)
```


Input (User Interaction)
-----------------------

### Using input() Function
* Accept input from the user.
* Example:
```py
name = input("Enter your name: ")
print(f"Hello, {name}!")
```