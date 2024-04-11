## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def include_commas(text):
    #Parameters:
    #   text: a string representing a word
    # Return:
    #   a word that starts with a captial letter ends with a comma

```


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""Given an empty string
It returns an empty string"""
read_string("")
# => ""

"""Given a string returns one captial word, add that word an expression mark assgined to it
"""
read_strings("My name is LIAM")
# => "my name is Liam!"

"""Given an string with no capitals,return the string with no addiontal changes"""
read_string("My name is bob")


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```python
from lib.grammar import read_string
```

Ensure all test function names are unique, otherwise pytest will ignore them!
