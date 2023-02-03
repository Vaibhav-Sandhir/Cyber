cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
plain = ""

for c in cipher:
    if(c == '{' or c == '}' or c == '_'):
        plain = plain + c
    else:    
        num = ord(c);
        if(c.isupper()):
            num = num - 65
            num = (num+13) % 26
            num = num + 65
        else:
            num = num - 97
            num = (num+13) % 26
            num = num + 97
        plain = plain + chr(num)
print(plain)            