list_cipher = [91,322,57,124,40,406,272,147,239,285,353,272,77,110,296,262,299,323,255,337,150,102]
plain_text = ""

for c in list_cipher:
    num = (c % 37)
    if(num == 36):
        plain_text += "_"
    elif(num >= 26 and num <= 35):
        num = num - 26
        plain_text += str(num)
    elif(num >= 0 and num <= 25):
        char = chr(num + 65)
        plain_text += char

print("picoCTF{" + plain_text + "}")    
                       