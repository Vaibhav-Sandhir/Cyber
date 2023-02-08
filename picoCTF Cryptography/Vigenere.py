#Very Important. The key is lenght matches the to only the number of alphabets in the text
#Dont use key alphabets on non alphabetical terms in the text

def decrypt(cipher,key):
    plain_text = ""
    j = 0
    for i in range(len(cipher)):
        c = cipher[i]
        print(j)
        k = key[j]
        if(ord(c) < 65 or (ord(c) > 90 and ord(c) < 97) or  ord(c) > 122):
            plain_text += c    
        else:
            y = ord(k) - 65
            if( ord(c) >= 97 and ord(c) <= 122):
                x = ((ord(c) - 97 - y) % 26) + 97
                plain_text += chr(x)
                j = (j + 1) % 5
            else:
                x = ((ord(c) - 65 - y) % 26) + 65
                plain_text += chr(x)
                j = (j + 1) % 5
    return plain_text            
                
                    
cipher = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}"
key = "CYLAB"
print(decrypt(cipher, key))        
    