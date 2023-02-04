cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
plain = ""

for c in cipher:
    if(ord(c) < 65 or (ord(c) > 90 and ord(c) < 97) or  ord(c) > 122):
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