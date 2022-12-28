plain_text = input("Enter string to be encrypted: ")
shift = int(input("Enter shift key: "))
plain_text = plain_text.lower()
cipher = ""
decipher = ""

for x in range(0,len(plain_text)):
    temp = int(ord(plain_text[x]) - 96)
    cipher = cipher + chr(((temp + shift) % 26) + 96)
    

for x in range(0,len(cipher)):
    temp = int(ord(cipher[x]) - 96)
    decipher = decipher + chr(((temp - shift) % 26) + 96)    


print("Cipher: ",cipher)
print("Decipher: ",decipher)