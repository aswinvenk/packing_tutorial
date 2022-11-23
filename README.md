Different symbols and their functions
=====================================
## This is a sample program to explain different symbols in Python

Installation
============

Once available in PIP, run the following to install:

```python
pip install symbols_testing_aswin
```

Importing
=========
```python
>>> from symbols_testing_aswin import example
```

Examples
========

# Display the symbols
```python
>>> example.display_symbols()
```

# Adding two numbers
This function takes 2 numbers and returns the sum of them
```python
>>> example.plus().add(3,2)
5
```

# Concatenating two strings
This function takes 2 strings and joins them
```python
>>> example.plus().concat('hello','world')
'helloworld'
```

# Subtracting two numbers
This function takes 2 numbers and returns the difference of them
```python
>>> example.minus().sub(1,2)
-1
```

# Multipling two numbers
This function takes 2 numbers and returns the product of them
```python
>>> example.star().mul(1,2)
2
```

# Duplicating a string
This function takes a string and returns the duplicates it.
If number not given, it duplicates it once.
```python

>>> example.star().duplicate('python')
'pythonpython'

>>> example.star().duplicate('python',3)
'pythonpythonpython'
```

# Dividing two numbers
This function takes 2 numbers and returns the division of them
```python
>>> example.slash().div(1,2)
0.5
```

# Remainder after dividing two numbers
This function takes 2 numbers, divides them and returns the remainder
```python
>>> example.percentage().mod(10,3)
1
```
# Random number between 0 to 100
This function takes 2 numbers, divides them and returns the remainder
```python
>>> example.random_number().zero_to_hundred()
1
```

Created by Aswin Venkat <aswinvenk8@gmail.com>