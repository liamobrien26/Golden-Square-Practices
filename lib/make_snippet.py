def make_snippet(input_string):
    words = input_string.split()
    if len(words) > 5:
        snippet = ' '.join(words[:5]) + '...'
    else:
        snippet = input_string
    return snippet

