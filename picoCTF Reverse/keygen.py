#sha256 is a cryptographic hash algortithim in the hashlib library
#The dynamic part of the key needs to decoded so revers the check key function in source code
#hexdigest return the data in hex format
#The decoded key will be can be crosschecked if it activates the full version
#The source code was checking the enetere key with hashlib.sha256 so we generated ourselves the hashlib.sha part

import hashlib
username_trial = b"MORTON"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

hash = hashlib.sha256(username_trial).hexdigest()

key_part_dynamic1_trial += hash[4]
key_part_dynamic1_trial += hash[5]
key_part_dynamic1_trial += hash[3]
key_part_dynamic1_trial += hash[6]
key_part_dynamic1_trial += hash[2]
key_part_dynamic1_trial += hash[7]
key_part_dynamic1_trial += hash[1]
key_part_dynamic1_trial += hash[8]

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)