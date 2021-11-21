#just for info purpose to create your own hash values
import hashlib

passwd = '1234'

result =hashlib.md5(passwd.encode())

print (result.hexdigest())
