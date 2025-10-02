# Seven-segment display patterns for digits 0-9 (13 LEDs, 3 columns x 5 rows)
digits = {
    '0': [
        "###",
        "# #",
        "# #",
        "# #",
        "###"
    ],
    '1': [
        "  #",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    '2': [
        "###",
        "  #",
        "###",
        "#  ",
        "###"
    ],
    '3': [
        "###",
        "  #",
        "###",
        "  #",
        "###"
    ],
    '4': [
        "# #",
        "# #",
        "###",
        "  #",
        "  #"
    ],
    '5': [
        "###",
        "#  ",
        "###",
        "  #",
        "###"
    ],
    '6': [
        "###",
        "#  ",
        "###",
        "# #",
        "###"
    ],
    '7': [
        "###",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    '8': [
        "###",
        "# #",
        "###",
        "# #",
        "###"
    ],
    '9': [
        "###",
        "# #",
        "###",
        "  #",
        "###"
    ]
}

def display_digit(digit):
    pattern = digits.get(digit, ["   "] * 5)
    for line in pattern:
        print(line)

# Example usage:
num = input("Enter a digit (0-9): ")
display_digit(num)