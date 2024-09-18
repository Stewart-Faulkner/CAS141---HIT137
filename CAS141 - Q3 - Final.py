def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    
    return encrypted_text
                     
#this is the encryption function 
                      
def decrypt(encrypted_text, key):
    text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            
            text += chr(shifted)
        else:
            text += char
    
    return text        
#this is the decryption function 
                      
#key for use int                      
key = 13

while True:
#Ask for input and encrypt (not req for assignment)
 original_code = (input("Code to be encrypted: "))
 encrypted_code = encrypt(original_code, key)
 print('Encrypted:', encrypted_code)

#ask for input and decrypt (essential)
 encrypted_code_insert = (input("Code to be decrypted: "))
 decrypted_code = decrypt(encrypted_code_insert, key)
 print('decrypt:', decrypted_code)