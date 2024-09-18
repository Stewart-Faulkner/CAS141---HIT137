def separate_string(s):
    if len(s) < 16:
        return "String too short"
    numbers = ''.join(char for char in s if char.isdigit())
    letters = ''.join(char for char in s if char.isalpha())
    return numbers, letters

def convert_even_numbers(number_string):
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_values = [ord(str(num)) for num in even_numbers]
    return even_numbers, ascii_values

def convert_uppercase_letters(letter_string):
    uppercase_letters = [char for char in letter_string if char.isupper()]
    ascii_values = [ord(char) for char in uppercase_letters]
    return uppercase_letters, ascii_values

def process_string(s):
    number_string, letter_string = separate_string(s)
    print(f"Separate them - {number_string} (number string) and {letter_string} (letter string).")
    
    even_numbers, number_ascii = convert_even_numbers(number_string)
    print("Convert the even numbers in the number string to ASCII Code Decimal Values")
    print(f"{even_numbers} (Even Numbers)")
    print(f"{number_ascii} (ASCII CODE)")
    
    uppercase_letters, letter_ascii = convert_uppercase_letters(letter_string)
    print("Convert the upper-case letter in letter string to ASCII Code Decimal Values.")
    print(f"{', '.join(uppercase_letters)} (Upper-case Letters)")
    print(f"{letter_ascii} (ASCII CODE Decimal Values)")

# Test the function
test_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
process_string(test_string)

# Function for the cryptogram part
def decrypt_cryptogram(cryptogram, shift):
    decrypted = ''
    for char in cryptogram:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted += char
    return decrypted

def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted = decrypt_cryptogram(cryptogram, shift)
        print(f"Shift {shift}: {decrypted}")

# Test the cryptogram decryption
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQ NG GVZRF UNEO GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
find_shift_key(cryptogram)
