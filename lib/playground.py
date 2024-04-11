def get_most_common_letter(text):
    counter = {}
    print(f"\nThis prints the list {counter}")
    for char in text: 
        counter[char] = counter.get(char, 0) 
    letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
