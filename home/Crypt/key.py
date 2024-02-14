import string

def generate_flag():
    ascii_values  = [84, 104, 82, 101, 65, 100, 83, 95, 66, 117, 83, 116, 69, 114, 83, 123, 66, 97, 37, 82, 42, 115, 80, 50, 95, 101, 88, 64, 97, 77, 36, 112, 76, 95, 101, 74, 111, 35, 72, 50, 110, 89, 95, 107, 37, 73, 110, 42, 71, 38, 115, 84,125]

    text == ''.join(chr(char) for char in ascii_values)
    print(text);

print(generate_flag());