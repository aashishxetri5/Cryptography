def getCipher(text, rails):
    
    ciphertext = ""
    length_row = 0

    #choosing in what interval a text is to be selected to arrange in a row.
    for i in range(rails):
        ctext = ''
        for j in range(i, len(text), rails):
            ctext = ctext + (plain_text[j]) 
        
        if i == 0:
            length_row = len(ctext) #setting length of first row to add extra alphabets later in other rows to match dimension

        if i != 0 and len(ctext) < length_row:
            ctext += 'X' #adding extra alphabet

        ciphertext += ctext #concatenating the finalised cipher part of a row into cipertext

        print(ctext)

    return ciphertext


def getDecipher(text, rails):

    deciphertext = ""
    length = int(len(text)/rails)
    
    for i in range(0, length):
        for j in range(0, rails):
            deciphertext += text[length*j + i]
    
    return deciphertext


#Input
plain_text = input("Enter the plain text: ").upper().replace(' ','')
rails = int(input("Enter the rails: "))

#Ciphered Text
cipher_text = getCipher(plain_text, rails)
print("Ciphered Text: " + cipher_text)

#Deciphered Text
decipher_text = getDecipher(cipher_text, rails)
print("Deciphered Text: " + decipher_text)