#Using website https://databorder.com/transfer/morse-sound-receiver/ to decode morse code audio

flag = "WH47 H47H 90D W20U9H7"
flag = flag.replace(" ","_")
flag = flag.lower()
print("picoCTF{" + flag + "}")