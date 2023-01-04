enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
hex_dec = ""

for c in enc:
    hex_dec = hex_dec + (hex(ord(c)).lstrip('0x'))   
                
        
print(bytes.fromhex(hex_dec).decode('ascii'))