import random as r

plain_text = 'Aashish Katwal'
# space_pos = plain_text.index(' ') #Storing the position of space

plain_text = plain_text.upper().replace(' ', '') #Removing spaces from the text

alphabets = {chr(65 + i): i for i in range(26)} #Generates all the alphabets with their indexing

key = r.randrange(1, 26) #Generates a number randomly to add to the text
encrypted_text = ""
decrypted_text = ""

#Reverse Dictionary
num_to_alphabet = {val: key for key, val in alphabets.items()}

#Encrypting text
for letter in plain_text:
    encr = (alphabets[letter] + key) % 26
    encrypted_text += num_to_alphabet[encr]

#Decrypting text
for letter in encrypted_text:
    decr = (alphabets[letter] - key) % 26
    decrypted_text += num_to_alphabet[decr]

print("Plain text: " + plain_text)
print("Encrypted Text: " + encrypted_text)
# print("Decrypted Text: " + decrypted_text[:space_pos] + " " + decrypted_text[space_pos:] )
print("Decrypted Text: " + decrypted_text)