#As the key is unknown I will be using brute force method
cipher = "dspttjohuifsvcjdpoabrkttds"

for key in range(1,26):
    plain = ""
    for c in cipher:
        num = ord(c) - 97
        num = (num + key) % 26
        num = num + 97 
        plain = plain + chr(num)
    print(plain)    