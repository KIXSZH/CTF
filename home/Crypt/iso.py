import random


def str_xor(secret, key):
    # extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])


flag_enc = chr(0x37) + chr(0x1c) + chr(0x34) + chr(0x06) + chr(0x35) + chr(0x02) + chr(0x30) + chr(0x2b) + chr(0x24) + chr(0x16) + chr(0x27) + chr(0x12) + chr(0x26) + chr(0x06) + chr(0x35) + chr(0x18) + chr(0x37) + chr(0x07) + chr(0x06) + chr(0x07) + chr(0x07) + chr(0x11) + chr(0x2b) + chr(0x25) + chr(0x0a) + chr(0x04) + chr(0x0e) + chr(0x06) + chr(0x06) + chr(0x39) + chr(0x07) + chr(0x11) + chr(0x05) + chr(0x11) + chr(0x0d) + chr(0x16) + chr(0x17) + chr(0x1d) + chr(0x09) + chr(0x0d) + chr(0x09)

num = random.choice(range(10, 101))

print('If ' + str(num) + ' is in decimal base, what is it in binary base?')

ans = input('Answer: ')

try:
    ans_num = int(ans, base=2)

    if ans_num == num:
        flag = str_xor(flag_enc, 'ctf')
        print('That is correct! Here\'s your flag: ' + flag)
    else:
        print(str(ans_num) + ' and ' + str(num) + ' are not equal.')

except ValueError:
    print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')