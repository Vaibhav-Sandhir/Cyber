enc = []
for i in range(0,32):
    enc.insert(i,'a')
 
    
print(enc)     
enc[0] = 'd' 
enc[29] = '3' 
enc[4] = 'r'
enc[2] = '5' 
enc[23] = 'r' 
enc[3] = 'c'
enc[17] = '4' 
enc[1] = '3' 
enc[7] = 'b' 
enc[10] = '_' 
enc[5] = '4' 
enc[9] = '3'
enc[11] = 't' 
enc[15] = 'c' 
enc[8] = 'l' 
enc[12] = 'H' 
enc[20] = 'c' 
enc[14] = '_' 
enc[6] = 'm' 
enc[24] = '5' 
enc[18] = 'r' 
enc[13] = '3' 
enc[19] = '4' 
enc[21] = 'T' 
enc[16] = 'H' 
enc[27] = 'f' 
enc[30] = 'b' 
enc[25] = '_' 
enc[22] = '3' 
enc[28] = '6' 
enc[26] = 'f' 
enc[31] = '0'
flag = ""
for c in enc:
    flag = flag + c

flag = "picoCTF{" + flag + "}"
print(flag)    

