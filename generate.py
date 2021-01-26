#-*- coding: utf-8 -*-

from passlib.context import CryptContext
crypt_context = CryptContext(
    ['pbkdf2_sha512', 'md5_crypt'],
    deprecated=['md5_crypt'],
)

password = raw_input('Proposed password: ')

password_hash = crypt_context.encrypt(password)

""" 
These lines will write the password and hash in the pass.txt file
"""
file = open('pass.txt', 'w')
file.write('Your password:\n')
file.write(password)
file.write('\nYour hash: ')
file.write('\n' + password_hash)
file.close()

""" 
Uncomment next lines to see the result on screen
"""
# file = open('pass.txt', 'r')

# print('\n')

# for line in file.readlines():
#     print(line)
    
# print('\n')

# file.close()

