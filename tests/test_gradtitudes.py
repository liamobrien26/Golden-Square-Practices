from lib.gradtitudes import Gratitudes

"""
Given multiple gratitudes
We can see a nice list of them
"""

def test_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("My cat")
    gratitudes.add("The sun")
    gratitudes.add("My friends")
    result = gratitudes.format()
    assert result == "I am grateful for: My cat, the sun, and my friends."