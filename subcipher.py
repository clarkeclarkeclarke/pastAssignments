import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "Hello world, my name is Clarke Roche"


def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))
