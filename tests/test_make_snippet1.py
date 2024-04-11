#A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
from lib.make_snippet import make_snippet


"""Given an empty string 
it returns an empty string"""

def test_make_snippet_that_returns_empty():
    result = make_snippet("")
    assert result == ""


"Given an string and return the same string as it was given"
def test_make_snippet():
    result = make_snippet("Hello, my name is Liam O'Brien. How are you?")
    assert result == "Hello, my name is Liam..."

def test_make_snippet_return_correct_values():
    result = make_snippet("Hi I am Liam. What is your name?")
    assert result == "Hi I am Liam. What..."

