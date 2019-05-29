#-*- coding: utf-8 -*-

from passlib.context import CryptContext
crypt_context = CryptContext(
    ['pbkdf2_sha512', 'md5_crypt'],
    deprecated=['md5_crypt'],
)

proposal = raw_input('Password propuesto: ')

password = crypt_context.encrypt(proposal)

file = open('pass.txt', 'w')

file.write(password)
file.write('\n' + proposal)

file.close()

file = open('pass.txt', 'r')

print('\n')

for line in file.readlines():
    print(line)
    
print('\n')

file.close()

