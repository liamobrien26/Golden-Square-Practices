from lib.count_words import count_words


# ""Input a string and returns a string"
# def test_countwords():
#     result = count_words("Hello, how are you?")
#     assert result == "Hello, how are you?"

def test_return_length():
    result = count_words("Hello, how are you?")
    assert result == 19