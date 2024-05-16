#password generator
import random
lower="abcderfhijklmopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}@#$%^&_-*"
all=lower+upper+numbers+symbols
length=16
for i in range(5):
    password=" ".join(random.sample(all,length))
    print(password)





