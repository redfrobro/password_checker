import hashlib
import requests


pw_hash = hashlib.sha1(b'Password1').hexdigest()

hash_list = requests.get('https://api.pwnedpasswords.com/range/{}'.format(pw_hash[:5]))

formatted_hash_list = hash_list.content.splitlines()

for pwned_hash in formatted_hash_list:
    if pw_hash[:5].upper() + pwned_hash.decode('ascii').split(':')[0] == pw_hash.upper():
        print(pw_hash[:5].upper() + pwned_hash.decode('ascii'))
