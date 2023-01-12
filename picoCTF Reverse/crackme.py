bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN"
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
rotate_const = 47
decoded = ""
for c in bezos_cc_secret:
    index = alphabet.find(c)
    original_index = (index + rotate_const) % len(alphabet)
    decoded = decoded + alphabet[original_index]

print(decoded)                                            