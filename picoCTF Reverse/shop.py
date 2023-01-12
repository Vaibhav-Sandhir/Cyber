#As mentioned in the hint exploit the edge cases which the source has not handled. buy 0 and quantity is -10
#Then buy flag

enc = [112 ,105 ,99 ,111 ,67 ,84 ,70 ,123 ,98 ,52 ,100 ,95 ,98 ,114 ,111 ,103 ,114 ,97 ,109 ,109 ,101 ,114 ,95 ,57 ,99 ,49 ,49,56 ,98 ,98 ,102 ,125]
flag = ""

for c in enc:
    flag = flag + chr(c)
    

print(flag)    