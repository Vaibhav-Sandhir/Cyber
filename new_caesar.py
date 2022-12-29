# Inside source file of new_caesar's.py 
# offset = 97
# Alphabet = abcdefghijklmnop
# Assert is x = 3 , assert x == 4 , will raise assertion error as x should be 3 
# first assertion is that key should in Alphabet i.e betweeen a - p
# second assertion is that key length is 1, should be 1 as ceaser's cipher
# The shift function is doing the caesar's shift but modulo 16 as we are taking alphabets a to p
# Extra step is the b16_encode which takes a string then one character at a time first converts the charcater to 
# its asccii then to it's binary consisiting of 8 digits which is = binary
# then [:4] takes the first 4 digits of binary and converts it into integer which is index then enc = enc + Alphabet[int]
# This was all how telling how the encryption has been done so how the encrypted string got generated 
# So to decode first we have to shift again then b16_decode on it.
# b16_decode has to do what b16_encode did but opposite so take 2 characters at time from cipher which will give 1 
# character deciphered. We will know the index of the character of cipher then convert into binary and concat with
# next one and then convert that binary to int and that into character 
# As we don't know key we will brute force it as it can be only between a and p
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


def b16_decode(cipher):
    decipher = ""
    for i in range(0,len(cipher),2):
        binary = "{0:04b}".format(ALPHABET.index(cipher[i])) + "{0:04b}".format(ALPHABET.index(cipher[i + 1]))
        decipher += chr(int(binary,2))  #, 2 tell the base is 2 for binary number
    return decipher    


cipher = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"


for key in ALPHABET:
    flag = ""
    print("Trying key : ", key)
    for c in cipher:
        flag += shift(c,key)
    print("Flag is: ", b16_decode(flag))    



