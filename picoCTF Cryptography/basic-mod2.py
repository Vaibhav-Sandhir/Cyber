list_cipher = [104,85,69,354,344,50,149,65,187,420,77,127,385,318,133,72,206,236,206,83,342,206,370]
plain_text = ""

for c in list_cipher:
    num = pow(c, -1, 41)
    if(num == 37):
        plain_text += "_"
    elif(num >= 27 and num <= 36):
        num = num - 27
        plain_text += str(num)
    elif(num >= 1 and num <= 26):
        char = chr(num + 64)
        plain_text += char

print("picoCTF{" + plain_text + "}")    