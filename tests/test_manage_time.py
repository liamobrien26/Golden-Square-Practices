from lib.manage_time import *

"""Passes string through"""
def testing_if_string_passing():
    result = manage_time("Hello")
    assert result == "Hello"

"""Returns time"""

def test_if_time_passing():
    result = manage_time(11)
    assert result == 11

"""Lets assume in one minute you can read 25 words"""
def test_text_read_in_minutes():
    result = returns_text(20)
    assert result == "Estimated reading time for 20 minutes is 500 words"
